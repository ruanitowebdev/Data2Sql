import json
from DB_Manager.Update_dataset import Update_data  
from  DB_Manager.Connect_database import connect
from  DB_Manager.dtypeTransform import dtype_columns
from  DB_Manager.getElement import getbase
from  DB_Manager.ReadDataset import read_dataset
from DB_Manager.dropduplicated import drop_duplicated
from sqlalchemy import text , select
import dotenv
import os
config = json.load(open("src/config.json" , encoding="utf-8"))

Update_data("vendastech2", config)