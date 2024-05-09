from cgi import print_exception
from typing import Union, List
from http import HTTPStatus
from pydantic import ValidationError
from models import UserModel, PaginationModel
from services import users_service
from db import supabase
from fastapi import APIRouter, Request
from utils.request_handler import throw_exception, response_json


router = APIRouter()

@router.post('/api/users')
def create_user(user: UserModel):
    user_email = user.email.lower()
    # TODO implement hashing for password
    hashed_password = user.password

    if users_service.user_exists(value=user_email):
        return throw_exception({ "message": "User already exists" }, HTTPStatus.NOT_ACCEPTABLE)

    user = users_service.create_user(user)

    if user:
        return response_json({"message": "User created successfully"})
    else:
        return throw_exception({"message": "User creation failed"}, HTTPStatus.INTERNAL_SERVER_ERROR)


@router.get('/api/users')
def get_users(req: Request):
    print("Error Not HAndled Corresponding Users")
    try:
        pagination: PaginationModel = PaginationModel(
            page=int(req.query_params.get('page', 1)),
            per_page=int(req.query_params.get('per_page', 10)),
            sort_by=req.query_params.get('sort_by', 'id'),
            sort_order=req.query_params.get('sort_order', 'asc'),
        )
        print(pagination);
        users = users_service.get_users(pagination=pagination)
        print("Error Not HAndled Corresponding Users 2222")
    except ValidationError as e:
        print_exception(e.json())
        return throw_exception(e.json(), HTTPStatus.INTERNAL_SERVER_ERROR)
    if users:
        print(users)
        return response_json(users.data)
    else:
        raise throw_exception({ "message": "Something went wrong!" }, HTTPStatus.INTERNAL_SERVER_ERROR)


@router.get('/api/users/{id}')
def get_user(id: Union[str] = None):
    print(id)
    if id:
        user = (
            supabase.from_("users")
            .select("id", "first_name", "last_name", "email")
            .limit(1)
            .eq("id", id)
            .execute()
        )
        print(user)
        if user:
            return { "data": user.data }
        else:
            raise throw_exception({"message": "User not found"}, HTTPStatus.NOT_FOUND)

@router.put('/api/users/{id}')
def update_user(id: str, email: str, name: str):
    user_email = email.lower()

    if user_exists(value=user_email):
        return {"message": "Email already exists"}
    user = (
        supabase.from_("users")
        .update({"name": name, "email": email})
        .eq("id", id)
        .execute()
    )

    if user:
        return {"message": "User updated successfully"}
    else:
        raise throw_exception({"message": "User update failed"})


@router.delete('/api/users/{id}')
def delete_user(id: str):
    if user_exists("id", id):
        supabase.from_("users").delete().eq("id", id).execute()
        return {"message": "User deleted successfully"}
    else:
        raise throw_exception({"message": "User deletion failed"})
