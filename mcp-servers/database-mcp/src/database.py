import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

SERVER = os.getenv("DB_SERVER")
DATABASE = os.getenv("DB_DATABASE")
USERNAME = os.getenv("DB_USERNAME")
PASSWORD = os.getenv("DB_PASSWORD")
DRIVER = os.getenv("DB_DRIVER")


from urllib.parse import quote_plus

PASSWORD = quote_plus(os.getenv("DB_PASSWORD"))

connection_string = (
    f"mssql+pyodbc://{USERNAME}:{PASSWORD}"
    f"@{SERVER}/{DATABASE}"
    f"?driver={DRIVER.replace(' ', '+')}"
    "&TrustServerCertificate=yes"
)


engine = create_engine(connection_string)

def get_connection():
    return engine.connect()