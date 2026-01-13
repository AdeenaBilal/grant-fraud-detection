import psycopg2

try:
    conn = psycopg2.connect(
        host="db.fpofoagkluwhoeikwoeh.supabase.co",
        port=5432,
        database="postgres",
        user="postgres",
        password="dumbleJune1994$",
        sslmode="require"
    )

    cur = conn.cursor()
    cur.execute("SELECT current_database(), current_user;")
    result = cur.fetchone()

    print("✅ Connected to Supabase successfully")
    print("Database:", result[0])
    print("User:", result[1])

    cur.close()
    conn.close()

except Exception as e:
    print("❌ Connection failed")
    print(e)
