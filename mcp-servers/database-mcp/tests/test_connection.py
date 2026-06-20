import pyodbc

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=DESKTOP-EOK41CC;"
    "DATABASE=LogisticsDB;"
    "UID=sa;"
    "PWD=Dalton@2014$;"
    "TrustServerCertificate=yes;"
)

print("Connected Successfully!")

cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM Shipments")

print(cursor.fetchone())

conn.close()