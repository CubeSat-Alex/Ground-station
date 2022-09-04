from logic.data import Data
from model.database import DataBase

database = DataBase()
jsn = database.getLogs()
for i in jsn:
    print(i)
