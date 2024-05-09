import bcrypt
from models import UserModel, PaginationModel
from db import supabase
from typing import List, Union

table_name = 'users'

def user_exists(key: str = "email", value: str = None):
    user_count = supabase.from_(table_name).select("COUNT(id)").eq(key, value).limit(1).execute()
    return len(user_count) > 0


def create_user(user: UserModel):
    user_email = user.email.lower()
    # TODO implement hashing for password
    # hashed_password = user.password
    hashed_password = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())
    print(hashed_password.decode('utf-8'))

    if user_exists(value=user_email):
        return {"message": "User already exists"}

    user = (
        supabase.from_(table_name)
        .insert(user)
        .execute()
    )

    print(user)
    if user:
        return {"message": "User created successfully"}
    else:
        raise Exception({"message": "User creation failed"})


def get_user(user_id: Union[str, None] = None):
    if user_id:
        user = (
            supabase.from_(table_name)
            .select("id", "name", "email")
            .eq("id", user_id)
            .execute()
        )
        if user:
            return user
        else:
            raise Exception({"message": "User not found"})

def get_users(pagination: PaginationModel):
    users = (supabase.from_(table_name)
        .select('*', count='exact')
        .order((pagination.sort_by), desc=(True if pagination.sort_order is 'desc' else False))
        .limit(pagination.per_page)
        .offset(pagination.per_page * (pagination.page-1))
        .execute()
    )
    return users


def update_user(user_id: str, email: str, name: str):
    user_email = email.lower()
    if user_exists(value=user_email):
        email_exists = (
            supabase.from_(table_name).select("*").eq("email", user_email).execute()
        )
        if len(email_exists.data) > 0:
            return {"message": "Email already exists"}
    user = (
        supabase.from_(table_name)
        .update({"name": name, "email": email})
        .eq("id", user_id)
        .execute()
    )
    if user:
        return {"message": "User updated successfully"}
    else:
        raise Exception({"message": "User update failed"})


def delete_user(user_id: str):
    if user_exists("id", user_id):
        supabase.from_(table_name).delete().eq("id", user_id).execute()
        return {"message": "User deleted successfully"}
    else:
        raise Exception({"message": "User deletion failed"})
