# app.py
from flask import Flask, request, jsonify
import pandas as pd
from supabase import create_client, Client
from services.grantee_service import get_grantee_by_email, insert_grantee
from utils.csv_validator import validate_grantee_csv


#import uuid
from flask_cors import CORS
from flask import Blueprint
import os

upload_grantees_bp = Blueprint("upload_grantees", __name__)
#CORS(upload_grantees_bp)
#CORS(app, origins=["http://localhost:3000"])


# -----------------------------
# Supabase config
SUPABASE_URL = "https://fpofoagkluwhoeikwoeh.supabase.co"
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")  # Make sure you set this env variable
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
# -----------------------------



@upload_grantees_bp.route("/upload-grantees", methods=["POST"])
def upload_grantees():
    if "file" not in request.files:
        return jsonify({"message": "No file part"}), 400

    file = request.files["file"]

    try:
        # Read CSV file into Pandas
        df = pd.read_csv(file)
        is_valid, msg = validate_grantee_csv(df)
        if not is_valid:
            return jsonify({"message": msg}), 400
        #print("COLUMNS RECEIVED:", list(df.columns))

         # Check required columns
        #required_cols = ["full_name", "email", "phone", "org_name"]
        #for col in required_cols:
            #if col not in df.columns:
                #return jsonify({"message": f"Missing required column: {col}"}), 400

        # Generate random application_id for each row
        #df["application_id"] = [str(uuid.uuid4()) for _ in range(len(df))]

        # Loop through each grantee and insert if not exists
        for _, row in df.iterrows():
            email = row["email"]

            # Check if grantee exists
            #res = supabase.table("grantees").select("*").eq("email", email).execute()
            existing = get_grantee_by_email(supabase, row["email"])
            if existing:
                grantee_id = existing["grantee_id"]
            else:
                new_grantee = insert_grantee(supabase, row.get("full_name"), row.get("email"), row.get("phone"), row.get("org_name"))
                grantee_id = new_grantee["grantee_id"]

            # Optional: store application_id in a separate grants table

        return jsonify({"message": f"{len(df)} grantees processed successfully!"})

    except Exception as e:
        return jsonify({"message": str(e)}), 500
