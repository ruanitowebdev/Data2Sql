import pyodbc
import  os, dotenv

dotenv.load_dotenv()
DATABASE = os.getenv("DATABASE")
DBUSER = os.getenv("DB_USER")
DBPASS = os.getenv("DB_PASS")
DBSERVER = os.getenv("DBSERVER")
conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    f"SERVER=localhost\SQLEXPRESS;"
    f"DATABASE={DATABASE};"
    "Trusted_Connection=yes;"
    "TrustServerCertificate=yes;",
    timeout=10
)

print("Conectado com sucesso!")