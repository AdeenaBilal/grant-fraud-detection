# grantee_service.py
from supabase import Client

def get_grantee_by_email(supabase: Client, email: str):
    res = supabase.table("grantees").select("*").eq("email", email).execute()
    if res.data and len(res.data) > 0:
        return res.data[0]
    return None

def insert_grantee(supabase: Client, full_name, email, phone=None, org_name=None):
    res = supabase.table("grantees").insert({
        "full_name": full_name,
        "email": email,
        "phone": phone,
        "org_name": org_name
    }).execute()
    return res.data[0] if res.data else None
