import pandas as pd
from sqlalchemy import create_engine

# Supabase/Postgres connection string
DB_URL = "postgresql://postgres:dumbleJune1994$@db.fpofoagkluwhoeikwoeh.supabase.co:5432/postgres"

engine = create_engine(DB_URL)

# Example: Read a table
df = pd.read_sql("SELECT * FROM applications", engine)
print(df)

# Example: Insert a CSV into the table
data = pd.read_csv("applications.csv")
data.to_sql("applications", engine, if_exists="append", index=False)
