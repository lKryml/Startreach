from core import url, key
from supabase import create_client, Client

supabase :Client = create_client(supabase_url=url, supabase_key=key)