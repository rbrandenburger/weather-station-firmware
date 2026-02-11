import adafruit_sht31d
import board

i2c = board.I2C()
sensor = adafruit_sht31d.SHT31D(i2c)

print(f"Celsius: {sensor.temperature}")
print(f"Humidity: {sensor.relative_humidity}")
