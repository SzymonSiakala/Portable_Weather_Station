# Portable Weather Station
My bachelor's thesis project using Raspberry Pi as a weather station.  RPi is used as a standalone device that will collect the data from sensors and upload it to the website. Application is running in a Docker container so no additional software installed on the device is needed. Data is stored in the SQL database and CSV files as a backup, the backend is made with use of Flask, frontend with JavaScript. On the website graphs with the data can be found and options to change the time interval on them. Website can be accessed by connecting with the RPi IP address and appropriate port, which is by default equal to 5000.

## Hardware requirements
• RPi with 8GB or 4GB of RAM, <br />
• TSL25911FN - digital ambient light sensor, for measuring visible light, <br />
• BME280 - for measuring temperature, humidity, and air pressure, <br />
• LTR390-UV-1 - for measuring UV rays, <br />
• SGP40 - for detecting ambient VOC. <br />
In the system presented a Environment Sensor HAT made by Waveshare was used. <br />

## Installation and activation procedure
User has to install the Docker software on the RPi and then run the appropriate command or Bash Script.
```
sudo docker pull szymsia398/standalone_app
sudo docker run -ti --privileged -d -p 5000:5000 -ti --mount type=bind,source="/home/raspberry"/data,target=/data szymsia398/standalone_app
```

## List of packages
• Adafruit-Blinka, <br />
• adafruit-circuitpython-bme280, <br />
• adafruit-circuitpython-ltr390, <br />
• adafruit-circuitpython-sgp40, <br /> 
• adafruit-circuitpython-tsl2591, <br />
• APScheduler, <br />
• click, <br />
• Flask, <br />
• Flask-restx, <br />
• Flask-SQLAlchemy, <br />
• numpy, <br />
• PyMySQL, <br />
• pyzmq, <br />
• RPi.GPIO, <br />
• Charts.js
