# Portable Weather Station
# Szymon Siąkała

# MODELS

from flask_sqlalchemy import SQLAlchemy

database = SQLAlchemy()

# Creating models of all tables.
class Illuminance(database.Model):
    __tablename__ = 'illuminance_table'
    id = database.Column(database.Integer, primary_key = True)
    time = database.Column(database.String, nullable = False)
    illuminance = database.Column(database.Float)

    def __init__(self, time, illuminance):
        self.time = time
        self.illuminance = illuminance
    
    def __repr__(self):
        return f"{self.time : self.illuminance}"    # Representing the data as a string.

class UV_index(database.Model):
    __tablename__ = 'uv_index_table'
    id = database.Column(database.Integer, primary_key = True)
    time = database.Column(database.String, nullable = False)
    uv_index = database.Column(database.Float)

    def __init__(self, time, uv_index):
        self.time = time
        self.uv_index = uv_index

    def __repr__(self):
        return f"{self.time : self.uv_index}"

class Temperature(database.Model):
    __tablename__ = 'temperature_table'
    id = database.Column(database.Integer, primary_key = True)
    time = database.Column(database.String, nullable = False)
    temperature = database.Column(database.Float)

    def __init__(self, time, temperature):
        self.time = time
        self.temperature = temperature

    def __repr__(self):
        return f"{self.time : self.temperature}"

class Humidity(database.Model):
    __tablename__ = 'humidity_table'
    id = database.Column(database.Integer, primary_key = True)
    time = database.Column(database.String, nullable = False)
    humidity = database.Column(database.Float)

    def __init__(self, time, humidity):
        self.time = time
        self.humidity = humidity

    def __repr__(self):
        return f"{self.time : self.humidity}"

class Air_pressure(database.Model):
    __tablename__ = 'air_pressure_table'
    id = database.Column(database.Integer, primary_key = True)
    time = database.Column(database.String, nullable = False)
    air_pressure = database.Column(database.Float)

    def __init__(self, time, air_pressure):
        self.time = time
        self.air_pressure = air_pressure

    def __repr__(self):
        return f"{self.time : self.air_pressure}"

class Altitude(database.Model):
    __tablename__ = 'altitude_table'
    id = database.Column(database.Integer, primary_key = True)
    time = database.Column(database.String, nullable = False)
    altitude = database.Column(database.Integer)

    def __init__(self, time, altitude):
        self.time = time
        self.altitude = altitude

    def __repr__(self):
        return f"{self.time : self.altitude}"

class Compensated_voc(database.Model):
    __tablename__ = 'compensated_voc_table'
    id = database.Column(database.Integer, primary_key = True)
    time = database.Column(database.String, nullable = False)
    compensated_voc = database.Column(database.Integer)

    def __init__(self, time, compensated_voc):
        self.time = time
        self.compensated_voc = compensated_voc

    def __repr__(self):
        return f"{self.time : self.compensated_voc}"