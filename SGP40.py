# Portable Weather Station
# Szymon Siąkała

# SGP40 SENSOR

import board
import adafruit_sgp40
import RPi.GPIO as GPIO
import time

class SGP40_class:
    def __init__(self):
        self.i2c = board.I2C()    # Initializing the I2C bus.
        self.sensor = adafruit_sgp40.SGP40(self.i2c)    # Initializing the sensor.
        
    def measurement(self):
        raw = self.sensor.raw    # Reading the raw gas measurements.
        return round(raw)

if __name__ == '__main__':
    sensor = SGP40_class()
    time_output = time.localtime()    # Recording current time.
    current_time = time.strftime("%H:%M:%S", time_output)    # Changing data format.
    print("============== ", current_time, " ==============")
    print('{:<20}{:>15}{:^5}'.format("Raw VOC:", sensor.measurement(), "ppm"))    # Displaying data in form of a table.