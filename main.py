import json
from DB_Manager.Update_dataset import Update_data  
from sqlalchemy import text , select
import dotenv
import os
config = json.load(open("src/config.json" , encoding="utf-8"))

Update_data("Vendastech", config)