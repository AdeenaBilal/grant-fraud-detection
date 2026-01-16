# application_service.py
from supabase import Client

def insert_application(supabase: Client, application_id, grantee_id, org_age, previous_grants, budget_request, address):
    res = supabase.table("applications").insert({
        "application_id": application_id,
        "grantee_id": grantee_id,
        "org_age": org_age,
        "previous_grants": previous_grants,
        "budget_request": budget_request,
        "address": address
    }).execute()
    return res.data[0] if res.data else None
