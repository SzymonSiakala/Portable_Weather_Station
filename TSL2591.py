# Portable Weather Station
# Szymon Siąkała

# TSL2591 SENSOR

import board
import adafruit_tsl2591
import RPi.GPIO as GPIO
import time

class TSL2591_class:
    def __init__(self):
        self.i2c = board.I2C()   # Initializing the I2C bus.
        self.sensor = adafruit_tsl2591.TSL2591(self.i2c)   # Initializing the sensor.
        self.sensor.gain = 0X00   # Setting sensor gain to 1x (bright light).

    def measurement(self):
        lux = self.sensor.lux   # Reading and calculating the light level in lux.
        return round(lux, 2)

if __name__ == '__main__':
    sensor = TSL2591_class()
    time_output = time.localtime()    # Recording current time.
    current_time = time.strftime("%H:%M:%S", time_output)    # Changing data format.
    print("============== ", current_time, " ==============")
    print('{:<20}{:>15}{:^5}'.format("Illuminance:", sensor.measurement(), "lux"))    # Displaying data in form of a table.