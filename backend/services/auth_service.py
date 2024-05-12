from db import supabase
from models import AuthModel

def signup(credentials: dict):
    print(credentials)
    return supabase.auth.sign_up(AuthModel(credentials))