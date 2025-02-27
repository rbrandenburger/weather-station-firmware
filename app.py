import Adafruit_DHT
import os
import datetime
import requests

if __name__ == "__main__":
    print("taking a reading")
    humidity, temp_c = Adafruit_DHT.read_retry(Adafruit_DHT.DHT22, 14)
    recorded_on = datetime.datetime.now(datetime.timezone.utc).isoformat()

    r = requests.post(
        f"{os.environ['WEATHER_APP_URL']}/readings/create",
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
