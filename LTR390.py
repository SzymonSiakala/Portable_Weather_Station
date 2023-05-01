# Portable Weather Station
# Szymon Siąkała

# LTR390 SENSOR

import board
import adafruit_ltr390
import RPi.GPIO as GPIO
import time

class LTR390_class:
    def __init__(self):
        self.i2c = board.I2C()    # Initializing the I2C bus.
        self.sensor = adafruit_ltr390.LTR390(self.i2c)    # Initializing the sensor.

    def measurement(self):
        uv = self.sensor.uvi    # Reading the calculated UV Index value
        return round(uv, 4)

if __name__ == '__main__':
    sensor = LTR390_class()
    time_output = time.localtime()    # Recording current time.
    current_time = time.strftime("%H:%M:%S", time_output)    # Changing data format.
    print("============== ", current_time, " ==============")
    print('{:<20}{:>15}{:^5}'.format("UV index:", sensor.measurement(), ""))    # Displaying data in form of a table.