from supabase import PostgrestAPIResponse, PostgrestAPIError
from .general_service import GeneralService
from models import PostsModel, PaginationModel
from db import supabase
from typing import List, Union

table_name = 'posts'

def post_exists(key: str = "email", value: str = None, id = None) -> bool:
    query = supabase.table(table_name=table_name).select("*").eq(key, value)
    if id:
        query = query.not_eq("id", id)
    post_count = query.limit(1).execute()
    return True if len(post_count.data) != 0 else False


def create_post(post: PostsModel):    
    post_json = post.model_dump(exclude=['createdAt', 'id'])
    [post, err] = GeneralService(table_name=table_name).create(post_json)
    if err is not None:
        print("Error: From Post Service", err)
    return [post, err]


def get_last_post_id(where: dict[str, any]):
    if where is None:
        return [None, None]
    try:
        query = supabase.table(table_name=table_name).select("id")
        for key, value in where:
            query = query.eq(key, value)
        post = query.order("id", desc=True).limit(1).execute()
    except PostgrestAPIError as err:
        return [None, err.json()]
    if len(post.data) == 0:
        return [0, None]
    return [post.data[0]['id'], None]
    

def get_post(id: int, where):
    where['id'] = id
    return GeneralService(table_name=table_name).find_one(where=where)

def get_posts(pagination: PaginationModel):
    return GeneralService(table_name=table_name)\
            .find(pagination=pagination, model=PostsModel)


def update_post(id: str, item, where: dict[str, any]):
    if where is None:
        return [None, None]
    try:
        post = GeneralService(table_name=table_name).update(where, item)
    except PostgrestAPIError as e:
        return[ None, e.json()]
    return [post, None]

def delete_post(id: str, profile_id: int = None) -> Union[PostgrestAPIResponse | None, PostgrestAPIError | None]:
    try:
        results = GeneralService(table_name=table_name, profile_id=profile_id).delete_by_id(id=id)
    except PostgrestAPIError as e:
        return[ None, e.json()]
    return [results, None]

