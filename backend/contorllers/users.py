from utils.logger import logger
from cgi import print_exception
from typing import Union, List
from http import HTTPStatus
from pydantic import ValidationError
from models import UserModel, PaginationModel
from services import users_service, auth_service
from services.auth_service import auth_protecter
from db import supabase
from fastapi import APIRouter, Request, Depends
from utils.request_handler import throw_exception, response_json, get_id_param


router = APIRouter()

@router.get('/api/users/check-email')
def check_email(req: Request):
    email = req.query_params.get('email')
    if not email:
        return throw_exception({ "message": "please provide the email" }, HTTPStatus.UNPROCESSABLE_ENTITY)
    if users_service.user_exists(value=email.lower(), key='email'):
        return throw_exception({ "message": "User already exists" }, HTTPStatus.NOT_ACCEPTABLE)
    else:
        return response_json({ "message": "Email is available" })


@router.post('/api/users')
def create_user(body: UserModel):
    # TODO implement hashing for password
    # if users_service.user_exists(value=body.email.lower(), key='email'):
    #     return throw_exception(
    #         Exception({ "message": "User already exists" }), HTTPStatus.NOT_ACCEPTABLE)

    [user, err] = users_service.create_user(body)
    if err:
        print(err)
        return throw_exception(err, status_code=HTTPStatus.UNPROCESSABLE_ENTITY)
    return response_json(user, HTTPStatus.CREATED) if user else throw_exception(
        err,
        HTTPStatus.UNPROCESSABLE_ENTITY
    )


@router.get('/api/users')
def get_users(req: Request, user: UserModel = Depends(auth_protecter)):
    if not user:
        return throw_exception({ "message": "Unauthorized!" }, status_code=HTTPStatus.UNAUTHORIZED)
    else:
        print("--------------------------------")
        print(user, "From Header Mocked")
        print("--------------------------------")
    try:
        pagination: PaginationModel = PaginationModel(
            page=int(req.query_params.get('page', 1)),
            per_page=int(req.query_params.get('per_page', 10)),
            sort_by=req.query_params.get('sort_by', 'id'),
            sort_order=req.query_params.get('sort_order', 'asc'),
        )
        [users, err] = users_service.get_users(pagination=pagination)
    except ValidationError as e:
        print_exception(e.json())
        return throw_exception(e, HTTPStatus.INTERNAL_SERVER_ERROR)
    if users:
        return response_json(users)
    else:
        return throw_exception(err if err else { "message": "Something went wrong!" }, HTTPStatus.INTERNAL_SERVER_ERROR)


@router.get('/api/users/{id}')
def get_user(id: Union[str]):
    id = get_id_param(id)
    if id is None or id < 0:
        return throw_exception({"message": "please provide the correct id"}, HTTPStatus.UNPROCESSABLE_ENTITY)
    user = users_service.get_user(id)
    print(user)
    if user:
        return { "data": user.data }
    else:
        return throw_exception({"message": "user not found"}, HTTPStatus.NOT_FOUND)

@router.put('/api/users/{id}')
def update_user(id: str, user: UserModel):
    id = get_id_param(id)
    if id is None or id < 0:
        return throw_exception({"message": "please provide the correct id"}, HTTPStatus.UNPROCESSABLE_ENTITY)
    
    [user, err] = users_service.update_user(id=id, item=user)
    if user:
        return response_json({ "message": "item updated successfully" })
    else:
        return throw_exception(err.json())


@router.delete('/api/users/{id}')
def delete_user(id: str):
    id = get_id_param(id)
    if id is None or id < 0:
        return throw_exception({"message": "please provide the correct id"}, HTTPStatus.UNPROCESSABLE_ENTITY)
    [results, err] = users_service.delete_user(id=id)
    if err:
        return throw_exception({"message": "failed to delete item"})
    else:
        return response_json(results,statusCode=HTTPStatus.OK)
