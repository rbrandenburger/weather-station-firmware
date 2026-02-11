import adafruit_sht31d
import board
import os
import datetime
import requests
from dotenv import load_dotenv

if __name__ == "__main__":
    print("taking a reading")

    load_dotenv()

    i2c = board.I2C()
    sensor = adafruit_sht31d.SHT31D(i2c)

    humidity = sensor.relative_humidity
    temp_c = sensor.temperature

    recorded_on = datetime.datetime.now(datetime.timezone.utc).isoformat()

    r = requests.post(
        f"{os.environ['WEATHER_APP_URL']}/api/readings",
        json={
            "temp_c": temp_c,
            "relative_humidity": humidity,
            "recorded_on": recorded_on
        },
        headers={
            "content-type": "application/json",
            "x-api-key": os.environ["WEATHER_APP_API_KEY"]
        }
    )

    print(r)
