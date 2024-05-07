from db import supabase
from models import User
from fastapi import APIRouter
from typing import Union
from crud import user_exists, create_user, get_user, update_user, delete_user
route = APIRouter()


# CREATE/POST
@route.post("/user")
def create_user(user: User):
    user_email = user.email.lower()
    # TODO implement hashing for password
    hashed_password = user.password
    # hashed_password = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())

    if user_exists(value=user_email):
        return {"message": "User already exists"}

    user = (
        supabase.from_("users")
        .insert({"name": user.name, "email": user_email, "password": hashed_password})
        .execute()
    )

    if user:
        return {"message": "User created successfully"}
    else:
        raise Exception({"message": "User creation failed"})


# GET
@route.get("/user")
def get_user(user_id: Union[str, None] = None):
    if user_id:
        user = (
            supabase.from_("users")
            .select("id", "name", "email")
            .eq("id", user_id)
            .execute()
        )
        if user:
            return user
        else:
            users = supabase.from_("users").select("*").execute()
        if users:
            return users
        else:
            raise Exception({"message": "User not found"})


# UPDATE/PUT
@route.put("/user")
def update_user(user_id: str, email: str, name: str):
    user_email = email.lower()

    if user_exists(value=user_email):
        email_exists = (
            supabase.from_("users").select("*").eq("email", user_email).execute()
        )
        if len(email_exists.data) > 0:
            return {"message": "Email already exists"}
    user = (
        supabase.from_("users")
        .update({"name": name, "email": email})
        .eq("id", user_id)
        .execute()
    )

    if user:
        return {"message": "User updated successfully"}
    else:
        raise Exception({"message": "User update failed"})


# DELETE
@route.delete("/user")
def delete_user(user_id: str):
    if user_exists("id", user_id):
        supabase.from_("users").delete().eq("id", user_id).execute()
        return {"message": "User deleted successfully"}
    else:
        raise Exception({"message": "User deletion failed"})