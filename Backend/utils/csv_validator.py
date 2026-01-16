# csv_validator.py
import pandas as pd

REQUIRED_GRANTEE_COLUMNS = ["full_name", "email", "phone", "org_name"]
REQUIRED_APPLICATION_COLUMNS = ["email", "org_age", "previous_grants", "budget_request", "address"]

def validate_grantee_csv(df: pd.DataFrame):
    df.columns = df.columns.str.strip()
    missing_cols = [col for col in REQUIRED_GRANTEE_COLUMNS if col not in df.columns]
    if missing_cols:
        return False, f"Missing columns: {', '.join(missing_cols)}"
    return True, "Valid CSV"

def validate_application_csv(df: pd.DataFrame):
    df.columns = df.columns.str.strip()
    missing_cols = [col for col in REQUIRED_APPLICATION_COLUMNS if col not in df.columns]
    if missing_cols:
        return False, f"Missing columns: {', '.join(missing_cols)}"
    return True, "Valid CSV"
