import bcrypt
from typing import Union
from backend.models.user import User
from fastapi import FastAPI
from backend.db.database import create_supabase_client

app = FastAPI()
