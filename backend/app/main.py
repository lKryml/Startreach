import os
import bcrypt
from app.models import User
from fastapi import FastAPI
from supabase import create_supabase_client

app = FastAPI()

supabase = create_supabase_client()


def user_exists(key: str = "email", value: str = None):
    user = supabase.from_("users").select('*').eq(key, value).execute()
    return len(user.data) > 0


@app.get("/")
def main_route():
    return {'message': 'Hello main route'}


@app.get("/health")
def health_check():
    return {'message': 'Healthy'}
