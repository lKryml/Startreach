from http import HTTPStatus
from pydantic import ValidationError
from models import PostsModel, PaginationModel, UserModel, UserTypes
from services import posts_service
from services.auth_service import auth_protecter
from fastapi import APIRouter, Request, Depends
from utils.request_handler import throw_exception, response_json, get_id_param, append_body, whereify


router = APIRouter()

@router.post('/api/posts')
async def create_post(body: PostsModel, user: UserModel = Depends(auth_protecter([UserTypes.ALL]))):
    [post, err] = posts_service.create_post(append_body(body, user))
    if err:
        return throw_exception(err, status_code=HTTPStatus.UNPROCESSABLE_ENTITY)
    return response_json(post.data[0], HTTPStatus.CREATED) if post else throw_exception(
        err,
        HTTPStatus.UNPROCESSABLE_ENTITY
    )


@router.get('/api/posts')
async def get_posts(req: Request, user: UserModel = Depends(auth_protecter())):
    try:
        pagination: PaginationModel = PaginationModel(
            page=int(req.query_params.get('page', 1)),
            per_page=int(req.query_params.get('per_page', 10)),
            sort_by=req.query_params.get('sort_by', 'id'),
            sort_order=req.query_params.get('sort_order', 'asc'),
            where=whereify(user)
        )
        [posts, err] = posts_service.get_posts(pagination=pagination)
    except ValidationError as e:
        return throw_exception(e, HTTPStatus.INTERNAL_SERVER_ERROR)
    if posts:
        return response_json(posts.data)
    else:
        return throw_exception(err if err else { "message": "Something went wrong!" }, HTTPStatus.INTERNAL_SERVER_ERROR)


@router.get('/api/posts/{id}')
async def get_post(id: str, user: UserModel = Depends(auth_protecter())):
    id = get_id_param(id)
    if id is None or id < 0:
        return throw_exception({"message": "please provide the correct id"}, HTTPStatus.UNPROCESSABLE_ENTITY)
    post = posts_service.get_post(id, where=whereify(user))
    if len(post.data) > 0:
        return response_json(post)
    else:
        return throw_exception({"message": "post not found"}, HTTPStatus.NOT_FOUND)

@router.put('/api/posts/{id}')
async def update_post(id: str, post: PostsModel, user: UserModel = Depends(auth_protecter)):
    id = get_id_param(id)
    if id is None or id < 0:
        return throw_exception({"message": "please provide the correct id"}, HTTPStatus.UNPROCESSABLE_ENTITY)

    post.profile_id = user.profile_id
    [updated_post, err] = posts_service.update_post(id=id, item=post)
    if updated_post:
        return response_json(updated_post)
    else:
        return throw_exception(err.json())


@router.delete('/api/posts/{id}')
async def delete_post(id: str, user: UserModel = Depends(auth_protecter)):
    id = get_id_param(id)
    if id is None or id < 0:
        return throw_exception({"message": "please provide the correct id"}, HTTPStatus.UNPROCESSABLE_ENTITY)
    [results, err] = posts_service.delete_post(id=id, where=whereify(user))
    if err:
        return throw_exception({"message": "failed to delete item"})
    else:
        return response_json(results,statusCode=HTTPStatus.OK)
