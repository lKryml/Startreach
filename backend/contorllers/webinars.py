from http import HTTPStatus
from pydantic import ValidationError
from models import WebinarsModel, PaginationModel, UserModel, UserTypes
from services import webinars_service
from services.auth_service import auth_protecter
from fastapi import APIRouter, Request, Depends
from utils.request_handler import throw_exception, response_json, get_id_param, append_body, whereify


router = APIRouter()

@router.post('/api/webinars')
async def create_webinar(body: WebinarsModel, user: UserModel = Depends(auth_protecter([UserTypes.ALL]))):
    [webinar, err] = webinars_service.create_webinar(append_body(body, user))
    if err:
        return throw_exception(err, status_code=HTTPStatus.UNPROCESSABLE_ENTITY)
    return response_json(webinar.data[0], HTTPStatus.CREATED) if webinar else throw_exception(
        err,
        HTTPStatus.UNPROCESSABLE_ENTITY
    )


@router.get('/api/webinars')
async def get_webinars(req: Request, user: UserModel = Depends(auth_protecter())):
    try:
        pagination: PaginationModel = PaginationModel(
            page=int(req.query_params.get('page', 1)),
            per_page=int(req.query_params.get('per_page', 10)),
            sort_by=req.query_params.get('sort_by', 'id'),
            sort_order=req.query_params.get('sort_order', 'asc'),
            where=whereify(user)
        )
        [webinars, err] = webinars_service.get_webinars(pagination=pagination)
    except ValidationError as e:
        return throw_exception(e, HTTPStatus.INTERNAL_SERVER_ERROR)
    if webinars:
        return response_json(webinars.data)
    else:
        return throw_exception(err if err else { "message": "Something went wrong!" }, HTTPStatus.INTERNAL_SERVER_ERROR)


@router.get('/api/webinars/{id}')
async def get_webinar(id: str, user: UserModel = Depends(auth_protecter())):
    id = get_id_param(id)
    if id is None or id < 0:
        return throw_exception({"message": "please provide the correct id"}, HTTPStatus.UNPROCESSABLE_ENTITY)
    webinar = webinars_service.get_webinar(id, where=whereify(user))
    if len(webinar.data) > 0:
        return response_json(webinar)
    else:
        return throw_exception({"message": "webinar not found"}, HTTPStatus.NOT_FOUND)

@router.put('/api/webinars/{id}')
async def update_webinar(id: str, webinar: WebinarsModel, user: UserModel = Depends(auth_protecter)):
    id = get_id_param(id)
    if id is None or id < 0:
        return throw_exception({"message": "please provide the correct id"}, HTTPStatus.UNPROCESSABLE_ENTITY)

    webinar.profile_id = user.profile_id
    [updated_webinar, err] = webinars_service.update_webinar(id=id, item=webinar)
    if updated_webinar:
        return response_json(updated_webinar)
    else:
        return throw_exception(err.json())


@router.delete('/api/webinars/{id}')
async def delete_webinar(id: str, user: UserModel = Depends(auth_protecter)):
    id = get_id_param(id)
    if id is None or id < 0:
        return throw_exception({"message": "please provide the correct id"}, HTTPStatus.UNPROCESSABLE_ENTITY)
    [results, err] = webinars_service.delete_webinar(id=id, where=whereify(user))
    if err:
        return throw_exception({"message": "failed to delete item"})
    else:
        return response_json(results,statusCode=HTTPStatus.OK)
