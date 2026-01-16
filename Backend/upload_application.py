# upload_application.py
from flask import request, jsonify
import pandas as pd
from supabase import create_client, Client
import uuid
import os
from flask import Blueprint
from utils.csv_validator import validate_application_csv
from services.application_service import insert_application
from services.grantee_service import get_grantee_by_email





# -----------------------------
# Supabase config
SUPABASE_URL = "https://fpofoagkluwhoeikwoeh.supabase.co"
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")  # Make sure you set this env variable
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
# -----------------------------

upload_application_bp = Blueprint("upload_application", __name__)


@upload_application_bp.route("/upload-application", methods=["POST"])
def upload_application():
    if "file" not in request.files:
        return jsonify({"message": "No file part"}), 400

    file = request.files["file"]

    try:
        # Read CSV into DataFrame
        df = pd.read_csv(file)
        is_valid, msg = validate_application_csv(df)
        if not is_valid:
            return jsonify({"message": msg}), 400


        for _, row in df.iterrows():

            email = row["email"]
            existing = get_grantee_by_email(supabase, email)

            if not existing:
                raise Exception(f"Grantee not found for email: {row['email']}")

            else:
                grantee_id = existing["grantee_id"]
                print("inserting application", flush=True)
                application_id = str(uuid.uuid4())
                insert_application(supabase, application_id, grantee_id, row.get("org_age"), row.get("previous_grants"), row.get("budget_request"), row.get("address"))

        return jsonify({"message": f"applications uploaded successfully!"})

    except Exception as e:
        return jsonify({"message": str(e)}), 500
