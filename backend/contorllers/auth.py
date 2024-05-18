from utils.logger import logger
from http import HTTPStatus
from pydantic import ValidationError
from models import AuthModel, TokenModel
from services import auth_service, users_service
from db import supabase
from fastapi import APIRouter, Request
from utils.request_handler import throw_exception, response_json

router = APIRouter()


@router.post('/auth/login')
def login(auth : AuthModel):
    [user, err] = auth_service.login(auth)
    if err is not None:
        return throw_exception(err, status_code=HTTPStatus.UNPROCESSABLE_ENTITY)
    return user

@router.post('/auth/register')
def register(auth: AuthModel):
    [user, err] = auth_service.register(auth)
    if err is not None:
        return throw_exception(err, status_code=HTTPStatus.UNPROCESSABLE_ENTITY)
    return user



@router.post('/auth/refresh_token')
def refresh_token(token: str):
    
    return response_json(auth)


@router.post('/auth/logout')
def logout():
    print("Logout User")
    return response_json(auth)