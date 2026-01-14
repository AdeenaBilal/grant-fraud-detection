# app.py
from flask import Flask, request, jsonify
import pandas as pd
from supabase import create_client, Client
import uuid
from flask_cors import CORS


app = Flask(__name__)
import os

app = Flask(__name__)
#CORS(app)
CORS(app, origins=["http://localhost:3000"])


# -----------------------------
# Supabase config
SUPABASE_URL = "https://fpofoagkluwhoeikwoeh.supabase.co"
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")  # Make sure you set this env variable
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
# -----------------------------



@app.route("/upload-grantees", methods=["POST"])
def upload_grantees():
    if "file" not in request.files:
        return jsonify({"message": "No file part"}), 400

    file = request.files["file"]

    try:
        # Read CSV file into Pandas
        df = pd.read_csv(file)
        print("COLUMNS RECEIVED:", list(df.columns))

         # Check required columns
        required_cols = ["full_name", "email", "phone", "org_name"]
        for col in required_cols:
            if col not in df.columns:
                return jsonify({"message": f"Missing required column: {col}"}), 400

        # Generate random application_id for each row
        df["application_id"] = [str(uuid.uuid4()) for _ in range(len(df))]

        # Loop through each grantee and insert if not exists
        for _, row in df.iterrows():
            email = row["email"]

            # Check if grantee exists
            #res = supabase.table("grantees").select("*").eq("email", email).execute()
            existing = (
            supabase
            .table("grantees")
            .select("grantee_id")
            .eq("email", email)
            .execute()
            )
            if existing.data and len(existing.data) > 0:
                grantee_id = existing.data[0]["grantee_id"]

            else:
                # Insert new grantee
                insert_res = supabase.table("grantees").insert({
                    "full_name": row["full_name"],
                    "email": row["email"],
                    "phone": row.get("phone"),
                    "org_name": row.get("org_name")
                }).execute()
                grantee_id = insert_res.data[0]["grantee_id"]

            # Optional: store application_id in a separate grants table

        return jsonify({"message": f"{len(df)} grantees processed successfully!"})

    except Exception as e:
        return jsonify({"message": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5000)
