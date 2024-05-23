from utils.logger import logger
from cgi import print_exception
from http import HTTPStatus
from pydantic import ValidationError
from models import ProjectsModel, PaginationModel, UserModel
from services import projects_service
from services.auth_service import auth_protecter
from fastapi import APIRouter, Request, Depends
from utils.request_handler import throw_exception, response_json, get_id_param


router = APIRouter()

@router.post('/api/projects')
def create_project(body: ProjectsModel, user: UserModel = Depends(auth_protecter)):
    [project, err] = projects_service.create_project(body)
    if err:
        return throw_exception(err, status_code=HTTPStatus.UNPROCESSABLE_ENTITY)
    return response_json(project.data[0], HTTPStatus.CREATED) if project else throw_exception(
        err,
        HTTPStatus.UNPROCESSABLE_ENTITY
    )


@router.get('/api/projects')
def get_projects(req: Request, user: UserModel = Depends(auth_protecter)):
    try:
        pagination: PaginationModel = PaginationModel(
            page=int(req.query_params.get('page', 1)),
            per_page=int(req.query_params.get('per_page', 10)),
            sort_by=req.query_params.get('sort_by', 'id'),
            sort_order=req.query_params.get('sort_order', 'asc'),
        )
        [projects, err] = projects_service.get_projects(pagination=pagination)
        print(projects.data, err)
    except ValidationError as e:
        return throw_exception(e, HTTPStatus.INTERNAL_SERVER_ERROR)
    if projects:
        return response_json(projects.data)
    else:
        return throw_exception(err if err else { "message": "Something went wrong!" }, HTTPStatus.INTERNAL_SERVER_ERROR)


@router.get('/api/projects/{id}')
def get_project(id: str):
    id = get_id_param(id)
    if id is None or id < 0:
        return throw_exception({"message": "please provide the correct id"}, HTTPStatus.UNPROCESSABLE_ENTITY)
    project = projects_service.get_project(id)
    if project:
        return response_json(project)
    else:
        return throw_exception({"message": "project not found"}, HTTPStatus.NOT_FOUND)

@router.put('/api/projects/{id}')
def update_project(id: str, project: ProjectsModel):
    id = get_id_param(id)
    if id is None or id < 0:
        return throw_exception({"message": "please provide the correct id"}, HTTPStatus.UNPROCESSABLE_ENTITY)
    
    [project, err] = projects_service.update_project(id=id, item=project)
    if project:
        return response_json(project)
    else:
        return throw_exception(err.json())


@router.delete('/api/projects/{id}')
def delete_project(id: str):
    id = get_id_param(id)
    if id is None or id < 0:
        return throw_exception({"message": "please provide the correct id"}, HTTPStatus.UNPROCESSABLE_ENTITY)
    [results, err] = projects_service.delete_project(id=id)
    if err:
        return throw_exception({"message": "failed to delete item"})
    else:
        return response_json(results,statusCode=HTTPStatus.OK)
