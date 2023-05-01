# Portable Weather Station
# Szymon Siąkała

# DATA LOADER

from csv import reader
import sqlalchemy

def data_importer(database, DataModel, file_path, fields : list, dtypes : list):
    try:
        file = open(file_path)    # Openning the file.
        reader = reader(file)    # Reading the CSV file.
        for i, row in enumerate(reader):    # Going through all rows of the file.
            data = {field: dtype(cell) for field, cell, dtype in zip(fields, row, dtypes)}    # Changing the data to a list with a structure similar to database records.
            record = DataModel(**data)
            database.session.add(record)    # Adding the record to the database.
        database.session.commit()
            
    except sqlalchemy.exc.IntegrityError:    # When error occurs rollback the changes.
        database.session.rollback()

    database.session.close()