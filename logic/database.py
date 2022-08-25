import json
import sqlite3
import pandas as pd

date = "date"
acceleration = "acceleration"
pressure = "pressure"
tempreture = "tempreture"
altitude = "altitude"
angleX = "angleX"
angleY = "angleY"
angleZ = "angleZ"
lat = "lat"
lang = "lang"
ldr1 = "ldr1"
ldr2 = "ldr2"
ldr3 = "ldr3"
ldr4 = "ldr4"

schema = '''
CREATE TABLE IF NOT EXISTS "telemetry" (
    "{}"	TEXT,
	"{}"	NUMERIC,
	"{}"	NUMERIC,
	"{}"	NUMERIC,
	"{}"	NUMERIC,
	"{}"	NUMERIC,
	"{}"	NUMERIC,
	"{}"	NUMERIC,
	"{}"	NUMERIC,
	"{}"	NUMERIC,
	"{}"	NUMERIC,
	"{}"	NUMERIC,
	"{}"	NUMERIC,
	"{}"	NUMERIC
);
'''.format(date, acceleration, pressure,
           tempreture, altitude,
           angleX, angleY, angleZ, lat,
           lang, ldr1, ldr2, ldr3, ldr4)


class DataBase:
    def __init__(self):
        self.connection = sqlite3.connect('database/data.db', check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.cursor.execute(schema)
        self.connection.commit()

    def dispose(self):
        self.connection.close()

    def addData(self, data):
        data = json.loads(data)
        print(data["acceleration"])
        accelerationFile = data["acceleration"].split('\n')
        pressureFile = data["pressure"].split('\n')
        angleFile = data["angle"].split('\n')
        gpsFile = data["gps"].split('\n')
        latFile = data["altitude"].split('\n')
        ldrFile = data["ldr"].split('\n')
        tempretureFile = data["tempreture"].split('\n')

        for index in range(len(accelerationFile)):
            dictionary = {date: accelerationFile[index].split(',')[0],
                          acceleration: accelerationFile[index].split(',')[1],
                          pressure: pressureFile[index].split(',')[1],
                          tempreture: tempretureFile[index].split(',')[1],
                          altitude: latFile[index].split(',')[1],
                          angleX: angleFile[index].split(',')[1],
                          angleY: angleFile[index].split(',')[2],
                          angleZ: angleFile[index].split(',')[3],
                          lat: gpsFile[index].split(',')[1],
                          lang: gpsFile[index].split(',')[2],
                          ldr1: ldrFile[index].split(',')[1],
                          ldr2: ldrFile[index].split(',')[1],
                          ldr3: ldrFile[index].split(',')[2],
                          ldr4: ldrFile[index].split(',')[3]}

            query = "insert into telemetry " + str(tuple(dictionary.keys())) + " values" + str(
                tuple(dictionary.values())) + ";"
            self.cursor.execute(query)
            self.connection.commit()

    def getLast30(self):
        df = pd.read_sql_query("SELECT * from telemetry", self.connection)
        return df.tail(30)

    def getData(self):
        df = pd.read_sql_query("SELECT * from telemetry", self.connection)
        df = df[::-1].reset_index()
        return df

    def export(self):
        df = pd.read_sql_query("SELECT * from telemetry", self.connection)
        df = df[::-1].reset_index()
        df.to_csv('database/export/database.csv', index=False)

