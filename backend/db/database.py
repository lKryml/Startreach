import os
from core import url, key
from supabase import create_client, Client



from supabase import create_client, Client

key="https://kcrqgiuagfzjqlrxxwzx.supabase.co"
url="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtjcnFnaXVhZ2Z6anFscnh4d3p4Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTQ3NTQ5NzEsImV4cCI6MjAzMDMzMDk3MX0.aJVtc1m-lJ5T5kK6sdMTu5RNGwm2z6u9i7jhjfhX7nA"

supabase :Client = create_client(key, url)
# def create_supabase_client() -> Client:
#     supabase: Client = create_client(url, key)
#     return supabase