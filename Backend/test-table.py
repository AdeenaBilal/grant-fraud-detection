# backend/db_setup.py
import psycopg2

# =========================
# 1️⃣ Database Connection
# =========================
DB_URL = "postgresql://postgres:dumbleJune1994$@db.fpofoagkluwhoeikwoeh.supabase.co:5432/postgres"

try:
    conn = psycopg2.connect(DB_URL)
    cur = conn.cursor()
    print("✅ Connected to Supabase successfully")
except Exception as e:
    print("❌ Connection failed:", e)
    exit(1)



cur.execute("""
CREATE TABLE IF NOT EXISTS connection_test (
    id SERIAL PRIMARY KEY,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
""")
conn.commit()
cur.close()
conn.close()
print("✅ Table created in Supabase")
