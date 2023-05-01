# Portable Weather Station
# Szymon Siąkała

# APP

from flask import Flask, render_template, redirect
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import date
import time
import random
import click

import BME280, LTR390, SGP40, TSL2591

from models import database, Illuminance, UV_index, Temperature, Humidity, Air_pressure, Altitude, Compensated_voc
from api import blueprint
from data_loader import data_importer

# Create objects of sensor classes.
TSL2591_object = TSL2591.TSL2591_class()
LTR390_object = LTR390.LTR390_class()
BME280_object = BME280.BME280_class()
SGP40_object = SGP40.SGP40_class()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Route used to clear the database and overwrite the files.
@app.route("/restart")
def restart():
    database.drop_all()
    database.create_all()
    file_path = "/data/illuminance.csv"
    open(file_path, "w").close()
    file_path = "/data/uv_index.csv"
    open(file_path, "w").close()
    file_path = "/data/temperature.csv"
    open(file_path, "w").close()
    file_path = "/data/humidity.csv"
    open(file_path, "w").close()
    file_path = "/data/air_pressure.csv"
    open(file_path, "w").close()
    file_path = "/data/altitude.csv"
    open(file_path, "w").close()
    file_path = "/data/compensated_voc.csv"
    open(file_path, "w").close()
    click.echo(click.style(f"Database and files has been erased.", fg = "red"))    # Messages for developers (not visible when the application is containerized).
    return redirect('/')

# Routes for different time intervals on the graphs.
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/week")
def week():
    return render_template("week.html")

@app.route("/today")
def today():
    return render_template("today.html") 

# Command used to load the measurements from files to the database.
@app.cli.command("load")
def load_data():
    try:
        data_importer(database, Illuminance, "/data/illuminance.csv", ["time", "illuminance"], [str, float])
        data_importer(database, UV_index, "/data/uv_index.csv", ["time", "uv_index"], [str, float])
        data_importer(database, Temperature, "/data/temperature.csv", ["time", "temperature"], [str, float])
        data_importer(database, Humidity, "/data/humidity.csv", ["time", "humidity"], [str, float])
        data_importer(database, Air_pressure, "/data/air_pressure.csv", ["time", "air_pressure"], [str, float])
        data_importer(database, Altitude, "/data/altitude.csv", ["time", "altitude"], [str, int])
        data_importer(database, Compensated_voc, "/data/compensated_voc.csv", ["time", "compensated_voc"], [str, int])
        return redirect('/')
    except:
        return redirect('/')

# Command used to create the tables in the database.
@app.cli.command("initialize")
def initialize(): 
    database.create_all() 

# Function used to save the measurement to the database.
def save_to_database(fields, row, dtypes, DataModel):
    with app.app_context():
        data = {field: dtype(cell) for field, cell, dtype in zip(fields, row, dtypes)}    # Changing the data to a list with a structure similar to database records.
        record = DataModel(**data)
        database.session.add(record)    # Adding the record to the database.
        database.session.commit()

# Function used to save the measurement to the file.
def save_to_file(file_path, file_input):
    try:
        file = open(file_path, 'r+')
        file.seek(0, 2)    # Placing the cursor at the end of the file.
    except OSError:
        click.echo(click.style(f"Database {file_path} not found, creating a new file...", fg = "red"))    # Messages for developers (not visible when the application is containerized).
        file = open(file_path, 'w+')
    file.write(file_input)
    file.close()

# Function used to take the measurements.
def measurement():
    illuminance = TSL2591_object.measurement()    # Calling a class method to get sensor data.
    uv_index = LTR390_object.measurement()
    temperature, humidity, air_pressure, altitude = BME280_object.measurement()
    compensated_voc = SGP40_object.sensor.measure_raw(temperature = temperature, relative_humidity = humidity)
    
    # When no sensors or RPi are available, replace the previous code with a random measure generator.
    """
    illuminance = round(random.uniform(130.00, 150.00), 2)
    uv_index = round(random.uniform(0.0, 5.0), 1)
    temperature = round(random.uniform(30.0, 35.0), 1)
    humidity = round(random.uniform(30.00, 40.00), 2)
    air_pressure = round(random.uniform(970.00, 980.00), 2)
    altitude = round(random.uniform(280, 290))
    compensated_voc = round(random.uniform(30200, 30500))
    """    

    time_output = time.localtime()    # Recording current time.
    current_time = time.strftime("%H:%M", time_output)    # Changing data format.
    date_output = date.today()    # Recording current date.
    current_date = date_output.strftime("%d.%m.%Y")    # Changing data format.
    time_variable = current_date + ' ' + current_time

    click.echo(click.style(f"Measuremrnt taken at: {time_variable}", fg = "yellow"))    # Messages for developers (not visible when the application is containerized).

    # Save the measurements to the database and files.
    fields = ["time", "illuminance"]
    row = [time_variable, str(illuminance)]
    dtypes = [str, float]
    save_to_database(fields, row, dtypes, Illuminance)
    file_path = "/data/illuminance.csv"
    file_input = "\"" + time_variable + "\"," + str(illuminance) + '\n'
    save_to_file(file_path, file_input)

    fields = ["time", "uv_index"]
    row = [time_variable, str(uv_index)]
    dtypes = [str, float]
    save_to_database(fields, row, dtypes, UV_index)
    file_path = "/data/uv_index.csv"
    file_input = "\"" + time_variable + "\"," + str(uv_index) + '\n'
    save_to_file(file_path, file_input)

    fields = ["time", "temperature"]
    row = [time_variable, str(temperature)]
    dtypes = [str, float]
    save_to_database(fields, row, dtypes, Temperature)
    file_path = "/data/temperature.csv"
    file_input = "\"" + time_variable + "\"," + str(temperature) + '\n'
    save_to_file(file_path, file_input)

    fields = ["time", "humidity"]
    row = [time_variable, str(humidity)]
    dtypes = [str, float]
    save_to_database(fields, row, dtypes, Humidity)
    file_path = "/data/humidity.csv"
    file_input = "\"" + time_variable + "\"," + str(humidity) + '\n'
    save_to_file(file_path, file_input)

    fields = ["time", "air_pressure"]
    row = [time_variable, str(air_pressure)]
    dtypes = [str, float]
    save_to_database(fields, row, dtypes, Air_pressure)
    file_path = "/data/air_pressure.csv"
    file_input = "\"" + time_variable + "\"," + str(air_pressure) + '\n'
    save_to_file(file_path, file_input)

    fields = ["time", "altitude"]
    row = [time_variable, str(altitude)]
    dtypes = [str, int]
    save_to_database(fields, row, dtypes, Altitude)
    file_path = "/data/altitude.csv"
    file_input = "\"" + time_variable + "\"," + str(altitude) + '\n'
    save_to_file(file_path, file_input)

    fields = ["time", "compensated_voc"]
    row = [time_variable, str(compensated_voc)]
    dtypes = [str, int]
    save_to_database(fields, row, dtypes, Compensated_voc)
    file_path = "/data/compensated_voc.csv"
    file_input = "\"" + time_variable + "\"," + str(compensated_voc) + '\n'
    save_to_file(file_path, file_input)

database.init_app(app)

app.register_blueprint(blueprint, url_prefix="/api")

click.clear()

scheduler = BackgroundScheduler()
scheduler.add_job(measurement, 'interval', seconds = 600)    # Adding a function responsible for taking measurements to the schedule.
scheduler.start()