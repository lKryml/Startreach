import os
from core.config import url, key
from supabase import create_client, Client

def create_supabase_client():
    supabase: Client = create_client(url, key)
    return supabase
