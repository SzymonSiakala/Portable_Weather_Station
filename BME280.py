# Portable Weather Station
# Szymon Siąkała

# BME280 SENSOR

import board
from adafruit_bme280 import basic as adafruit_bme280
import RPi.GPIO as GPIO
import time

class BME280_class:
    def __init__(self):
        self.i2c = board.I2C()    # Initializing the I2C bus.
        self.sensor = adafruit_bme280.Adafruit_BME280_I2C(self.i2c, address = 0x76)    # Initializing the sensor.
        self.sensor.sea_level_pressure = 1013.25    # Location's pressure (hPa) at sea level.

    def measurement(self):
        temp = self.sensor.temperature    # Reading the temperature value.
        hum = self.sensor.relative_humidity    # Reading the relative humidity value.
        pres = self.sensor.pressure    # Reading the pressure value.
        alt = self.sensor.altitude    # Reading the altitude value.
        return round(temp, 1), round(hum, 1), round(pres, 2), round(alt)

if __name__ == '__main__':
    sensor = BME280_class()
    time_output = time.localtime()    # Recording current time.
    current_time = time.strftime("%H:%M:%S", time_output)    # Changing data format.
    temp, hum, pres, alt = sensor.measurement()
    text = [["Temperature:", temp, "C"],    # Creating data array.
            ["Humidity:", hum, "%"],
            ["Air pressure:", pres, "hPa"],
            ["Altitude:", alt, "m"]]
    print("============== ", current_time, " ==============")
    for i in range(len(text)):
        print('{:<20}{:>15}{:^5}'.format(text[i][0], text[i][1], text[i][2]))    # Displaying data in form of a table.