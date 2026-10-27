
from pathlib import Path

import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL

CSV_FILE = Path("employee_clean.csv")

if not CSV_FILE.exists():
    raise FileNotFoundError(f"File not found: {CSV_FILE.resolve()}")

df = pd.read_csv(CSV_FILE, parse_dates=["Join_Date"])

connection_url = URL.create(
    "mssql+pyodbc",
    host="ALMONMON",
    database="EmployeeDataEngineering",
    query={
        "driver": "ODBC Driver 18 for SQL Server",
        "trusted_connection": "yes",
        "Encrypt": "yes",
        "TrustServerCertificate": "yes",
    },
)

engine = create_engine(connection_url, fast_executemany=True)

try:
    with engine.begin() as connection:
        existing_count = connection.execute(
            text("SELECT COUNT(*) FROM dbo.Employees")
        ).scalar_one()

        if existing_count > 0:
            raise RuntimeError(
                f"Table already contains {existing_count} rows. "
                "No data was inserted."
            )

        df.to_sql(
            name="Employees",
            con=connection,
            schema="dbo",
            if_exists="append",
            index=False,
            chunksize=1000,
        )

    print(f"Successfully loaded {len(df)} rows into dbo.Employees.")

finally:
    engine.dispose()
