from http import HTTPStatus
from pydantic import ValidationError
from models import UserModel, PaginationModel, UserTypes
from services import users_service, auth_service
from services.auth_service import auth_protecter
from fastapi import APIRouter, Request, Depends
from utils.request_handler import throw_exception, response_json, get_id_param, append_body, whereify


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
async def create_user(body: UserModel, user: UserModel = Depends(auth_protecter([UserTypes.ALL]))):
    [user, err] = auth_service.create_user(append_body(body, user))
    if err:
        return throw_exception(err, status_code=HTTPStatus.UNPROCESSABLE_ENTITY)
    return response_json(user.data[0], HTTPStatus.CREATED) if user else throw_exception(
        err,
        HTTPStatus.UNPROCESSABLE_ENTITY
    )


@router.get('/api/users')
async def get_users(req: Request, user: UserModel = Depends(auth_protecter())):
    try:
        pagination: PaginationModel = PaginationModel(
            page=int(req.query_params.get('page', 1)),
            per_page=int(req.query_params.get('per_page', 10)),
            sort_by=req.query_params.get('sort_by', 'id'),
            sort_order=req.query_params.get('sort_order', 'asc'),
            where=whereify(user)
        )
        [users, err] = auth_service.get_users(pagination=pagination)
    except ValidationError as e:
        return throw_exception(e, HTTPStatus.INTERNAL_SERVER_ERROR)
    if users:
        return response_json(users.data)
    else:
        return throw_exception(err if err else { "message": "Something went wrong!" }, HTTPStatus.INTERNAL_SERVER_ERROR)


@router.get('/api/users/{id}')
async def get_user(id: str, user: UserModel = Depends(auth_protecter())):
    id = get_id_param(id)
    if id is None or id < 0:
        return throw_exception({"message": "please provide the correct id"}, HTTPStatus.UNPROCESSABLE_ENTITY)
    [user, err] = auth_service.get_user(id, where=whereify(user))
    if len(user.data) > 0:
        return response_json(user.data[0])
    else:
        return throw_exception({"message": "user not found"}, HTTPStatus.NOT_FOUND)

@router.put('/api/users/{id}')
async def update_user(id: str, item: UserModel, user: UserModel = Depends(auth_protecter)):
    id = get_id_param(id)
    if id is None or id < 0:
        return throw_exception({"message": "please provide the correct id"}, HTTPStatus.UNPROCESSABLE_ENTITY)

    item.profile_id = user.profile_id
    [updated_user, err] = auth_service.update_user(id=id, item=item)
    if updated_user:
        return response_json(updated_user)
    else:
        return throw_exception(err.json())


@router.delete('/api/users/{id}')
async def delete_user(id: str, user: UserModel = Depends(auth_protecter)):
    id = get_id_param(id)
    if id is None or id < 0:
        return throw_exception({"message": "please provide the correct id"}, HTTPStatus.UNPROCESSABLE_ENTITY)
    [results, err] = auth_service.delete_user(id=id, where=whereify(user))
    if err:
        return throw_exception({"message": "failed to delete item"})
    else:
        return response_json(results,statusCode=HTTPStatus.OK)
