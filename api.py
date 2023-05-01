# Portable Weather Station
# Szymon Siąkała

# API

from flask import Blueprint
from flask_restx import Api, Resource, fields
import datetime
import time
import numpy as np

from models import Illuminance, UV_index, Temperature, Humidity, Air_pressure, Altitude, Compensated_voc

blueprint = Blueprint('api', __name__)
api = Api(blueprint)

# Function used to determine measurement indexes within a given time frame (offset).
def interval(DataModel, offset):
    time_output = time.time() - offset    # Calculation of the initial measurement timestamp that can be displayed on the graph.
    index = -1
    all_records = np.asarray(DataModel.query.all())    # Changing the list obtained from the query to an array to simplify the operation.
    for i in range(all_records.shape[0]):    # Going through the whole array.
        temp = all_records[i].time
        element = datetime.datetime.strptime(temp, "%d.%m.%Y %H:%M")
        tuple = element.timetuple()
        timestamp = time.mktime(tuple)    # Changing the string with time and date to a timestamp.
        if time_output < timestamp:    # Comparing both values to find the first value that can be displayed on the graph.
            index = i
            break
    if index >= 0:
        return index
    else:
        return -1
        
# Models creation.
illuminance_model = api.model("Illuminance", {
    "time": fields.String,
    "illuminance": fields.Float
})

uv_index_model = api.model("UV_index", {
    "time": fields.String,
    "uv_index": fields.Float
})

temperature_model = api.model("Temperature", {
    "time": fields.String,
    "temperature": fields.Float
})

humidity_model = api.model("Humidity", {
    "time": fields.String,
    "humidity": fields.Float
})

air_pressure_model = api.model("Air_pressure", {
    "time": fields.String,
    "air_pressure": fields.Float
})

altitude_model = api.model("Altitude", {
    "time": fields.String,
    "altitude": fields.Integer
})

compensated_voc_model = api.model("Compensated_voc", {
    "time": fields.String,
    "compensated_voc": fields.Integer
})

# Creating API routes that are used by Chart.js graphs.
@api.route("/Illuminance/<string:mode>")
class IlluminanceAPI(Resource):
    
    @api.marshal_with(illuminance_model,  envelope='data')
    def get(self, mode):
        if int(mode) == 2:
            index = interval(Illuminance, 7 * 24 * 60 * 60)
            if index >= 0:
                index = index + 1
                return Illuminance.query.filter(Illuminance.id >= index).all()
        if int(mode) == 3:
            index = interval(Illuminance, 24 * 60 * 60)
            if index >= 0:
                index = index + 1
                return Illuminance.query.filter(Illuminance.id >= index).all()
        return Illuminance.query.all()

@api.route("/UV_index/<string:mode>")
class UV_indexAPI(Resource):
    
    @api.marshal_with(uv_index_model,  envelope='data')
    def get(self, mode):    # Based on the value provided by the graph, appropriate database elements are returned.
        if int(mode) == 2:    # When mode = 2 the values from last week are selected.
            index = interval(UV_index, 7 * 24 * 60 * 60)
            if index >= 0:
                index = index + 1
                return UV_index.query.filter(UV_index.id >= index).all()
        if int(mode) == 3:    # When mode = 2 the values from last day are selected.
            index = interval(UV_index, 24 * 60 * 60)
            if index >= 0:
                index = index + 1
                return UV_index.query.filter(UV_index.id >= index).all()
        return UV_index.query.all()    # When mode = 1 or no measurements are old enough, whole database is selected.

@api.route("/Temperature/<string:mode>")
class TemperatureAPI(Resource):
    
    @api.marshal_with(temperature_model,  envelope='data')
    def get(self, mode):
        if int(mode) == 2:
            index = interval(Temperature, 7 * 24 * 60 * 60)
            if index >= 0:
                index = index + 1
                return Temperature.query.filter(Temperature.id >= index).all()
        if int(mode) == 3:
            index = interval(Temperature, 24 * 60 * 60)
            if index >= 0:
                index = index + 1
                return Temperature.query.filter(Temperature.id >= index).all()
        return Temperature.query.all()

@api.route("/Humidity/<string:mode>")
class HumidityAPI(Resource):
    
    @api.marshal_with(humidity_model,  envelope='data')
    def get(self, mode):
        if int(mode) == 2:
            index = interval(Humidity, 7 * 24 * 60 * 60)
            if index >= 0:
                index = index + 1
                return Humidity.query.filter(Humidity.id >= index).all()
        if int(mode) == 3:
            index = interval(Humidity, 24 * 60 * 60)
            if index >= 0:
                index = index + 1
                return Humidity.query.filter(Humidity.id >= index).all()
        return Humidity.query.all()

@api.route("/Air_pressure/<string:mode>")
class Air_pressureAPI(Resource):
    
    @api.marshal_with(air_pressure_model,  envelope='data')
    def get(self, mode):
        if int(mode) == 2:
            index = interval(Air_pressure, 7 * 24 * 60 * 60)
            if index >= 0:
                index = index + 1
                return Air_pressure.query.filter(Air_pressure.id >= index).all()
        if int(mode) == 3:
            index = interval(Air_pressure, 24 * 60 * 60)
            if index >= 0:
                index = index + 1
                return Air_pressure.query.filter(Air_pressure.id >= index).all()
        return Air_pressure.query.all()

@api.route("/Altitude/<string:mode>")
class AltitudeAPI(Resource):
    
    @api.marshal_with(altitude_model,  envelope='data')
    def get(self, mode):
        if int(mode) == 2:
            index = interval(Altitude, 7 * 24 * 60 * 60)
            if index >= 0:
                index = index + 1
                return Altitude.query.filter(Altitude.id >= index).all()
        if int(mode) == 3:
            index = interval(Altitude, 24 * 60 * 60)
            if index >= 0:
                index = index + 1
                return Altitude.query.filter(Altitude.id >= index).all()
        return Altitude.query.all()

@api.route("/Compensated_voc/<string:mode>")
class Compensated_vocAPI(Resource):
    
    @api.marshal_with(compensated_voc_model,  envelope='data')
    def get(self, mode):
        if int(mode) == 2:
            index = interval(Compensated_voc, 7 * 24 * 60 * 60)
            if index >= 0:
                index = index + 1
                return Compensated_voc.query.filter(Compensated_voc.id >= index).all()
        if int(mode) == 3:
            index = interval(Compensated_voc, 24 * 60 * 60)
            if index >= 0:
                index = index + 1
                return Compensated_voc.query.filter(Compensated_voc.id >= index).all()
        return Compensated_voc.query.all()