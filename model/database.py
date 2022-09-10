import json
import sqlite3
import pandas as pd

date = "date"
orbit = "orbit"
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

orbit = "orbit"
details = "details"
state = "state"

telemetryShema = f'''
CREATE TABLE IF NOT EXISTS "telemetry" (
    "{date}"	TEXT,
	"{orbit}"	NUMERIC,
	"{acceleration}"	NUMERIC,
	"{pressure}"	NUMERIC,
	"{tempreture}"	NUMERIC,
	"{altitude}"	NUMERIC,
	"{angleX}"	NUMERIC,
	"{angleY}"	NUMERIC,
	"{angleZ}"	NUMERIC,
	"{lat}"	NUMERIC,
	"{lang}"	NUMERIC,
	"{ldr1}"	NUMERIC,
	"{ldr2}"	NUMERIC,
	"{ldr3}"	NUMERIC,
	"{ldr4}"	NUMERIC
);
'''

logsSchema = f'''
CREATE TABLE IF NOT EXISTS "logs" (
	"{date}"	TEXT,
	"{orbit}"	INTEGER,
	"{details}"	TEXT,
	"{state}"	TEXT
);
'''

planSchema = f'''
CREATE TABLE IF NOT EXISTS "plan" (
	"from"	TEXT,
	"to"	TEXT,
    "id"	INTEGER,
	PRIMARY KEY("id" AUTOINCREMENT)
);
'''


class DataBase:
    def __init__(self):
        self.connection = sqlite3.connect('database/data.db', check_same_thread=False)
        self.cursor = self.connection.cursor()
        self.cursor.execute(telemetryShema)
        self.cursor.execute(logsSchema)
        self.cursor.execute(planSchema)
        self.connection.commit()

    def dispose(self):
        self.connection.close()

    def addPlan(self, plan):
        query = "insert into plan " + str(tuple(plan.keys())) + " values" + str(
                tuple(plan.values())) + ";"
        self.cursor.execute(query)
        self.connection.commit()
    
    def getPlanes(self):
         df = pd.read_sql_query("SELECT * from plan", self.connection)
         return df.to_dict('records')
        
    def deletePlan(self):
        query = '''DELETE FROM plan WHERE ID=(SELECT MAX(id) FROM plan)'''
        self.cursor.execute(query)
        self.connection.commit()

    def addLogs(self, logs):

        data = json.loads(logs).split('\n')
        print(len(data))
       
        for index in range(len(data)):
            dictionary = {date: data[index].split(',')[0],
                          orbit: data[index].split(',')[1],
                          details: data[index].split(',')[2],
                          state: data[index].split(',')[3]}
            query = "insert into logs " + str(tuple(dictionary.keys())) + " values" + str(
                tuple(dictionary.values())) + ";"
            self.cursor.execute(query)
            self.connection.commit()

    def getLogs(self): 
        df = pd.read_sql_query("SELECT * from logs", self.connection)
        df = df[::-1].reset_index()
        return df

    def addData(self, data):
        data = json.loads(str(data))
        accelerationFile = data["acceleration"].split('\n')
        pressureFile = data["pressure"].split('\n')
        angleFile = data["angle"].split('\n')
        gpsFile = data["gps"].split('\n')
        latFile = data["altitude"].split('\n')
        ldrFile = data["ldr"].split('\n')
        tempretureFile = data["tempreture"].split('\n')

        for index in range(len(accelerationFile)):
            dictionary = {date: accelerationFile[index].split(',')[0],
                          orbit: accelerationFile[index].split(',')[1],
                          acceleration: accelerationFile[index].split(',')[2],
                          pressure: pressureFile[index].split(',')[2],
                          tempreture: tempretureFile[index].split(',')[2],
                          altitude: latFile[index].split(',')[2],
                          angleX: angleFile[index].split(',')[2],
                          angleY: angleFile[index].split(',')[3],
                          angleZ: angleFile[index].split(',')[4],
                          lat: gpsFile[index].split(',')[2],
                          lang: gpsFile[index].split(',')[3],
                          ldr1: ldrFile[index].split(',')[2],
                          ldr2: ldrFile[index].split(',')[2],
                          ldr3: ldrFile[index].split(',')[3],
                          ldr4: ldrFile[index].split(',')[4]}

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

