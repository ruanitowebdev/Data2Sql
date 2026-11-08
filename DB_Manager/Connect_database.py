import os
from urllib.parse import quote_plus
from sqlalchemy import create_engine , text
import dotenv

def connect_database():
    dotenv.load_dotenv()
    DB_USER = os.getenv("DB_USER")
    DB_PASS = os.getenv("DB_PASS")
    DATABASE = os.getenv("DATABASE")
    DBSERVER = os.getenv("DBSERVER")
    
    # Tratamento essencial para caracteres especiais na senha e barras no servidor
    safe_pass = quote_plus(DB_PASS) 
    safe_server = quote_plus(DBSERVER) 
    
    engine = create_engine(
        f"mssql+pyodbc://{DB_USER}:{safe_pass}@{safe_server}/{DATABASE}"
        f"?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=no"
    )
    return engine
connect = connect_database

engine = connect_database() 
with engine.connect() as conn:
    result =  conn.execute(text("select 'hello'"))
    print(result.all())