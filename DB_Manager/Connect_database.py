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
    
    connection_string = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    f"SERVER={DBSERVER};"
    f"DATABASE={DATABASE};"
    f"UID={DB_USER};"
    f"PWD={DB_PASS};"
    "TrustServerCertificate=yes;"
)
    engine = create_engine(
        "mssql+pyodbc:///?odbc_connect="
        + quote_plus(connection_string)
    )
    return engine
connect = connect_database

engine = connect_database() 
with engine.connect() as conn:
    result =  conn.execute(text("select 'hello'"))
    print(result.all())