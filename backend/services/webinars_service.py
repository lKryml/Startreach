from supabase import PostgrestAPIResponse, PostgrestAPIError
from .general_service import GeneralService
from models import WebinarsModel, PaginationModel
from db import supabase
from typing import List, Union

table_name = 'webinars'

def webinar_exists(key: str = "email", value: str = None, id = None) -> bool:
    query = supabase.table(table_name=table_name).select("*").eq(key, value)
    if id:
        query = query.not_eq("id", id)
    webinar_count = query.limit(1).execute()
    return True if len(webinar_count.data) != 0 else False


def create_webinar(webinar: WebinarsModel):    
    webinar_json = webinar.model_dump(exclude=['createdAt', 'id'])
    webinar_json['start_date'] = webinar.start_date.date().isoformat()
    webinar_json['end_date'] = webinar.end_date.date().isoformat()
    [webinar, err] = GeneralService(table_name=table_name).create(webinar_json)
    if err is not None:
        print("Error: From Webinar Service", err)
    return [webinar, err]


def get_last_webinar_id(where: dict[str, any]):
    if where is None:
        return [None, None]
    try:
        query = supabase.table(table_name=table_name).select("id")
        for key, value in where:
            query = query.eq(key, value)
        webinar = query.order("id", desc=True).limit(1).execute()
    except PostgrestAPIError as err:
        return [None, err.json()]
    if len(webinar.data) == 0:
        return [0, None]
    return [webinar.data[0]['id'], None]
    

def get_webinar(id: int, where):
    where['id'] = id
    return GeneralService(table_name=table_name).find_one(where=where)

def get_webinars(pagination: PaginationModel):
    return GeneralService(table_name=table_name)\
            .find(pagination=pagination, model=WebinarsModel)


def update_webinar(id: str, item, where: dict[str, any]):
    if where is None:
        return [None, None]
    try:
        webinar = GeneralService(table_name=table_name).update(where, item)
    except PostgrestAPIError as e:
        return[ None, e.json()]
    return [webinar, None]

def delete_webinar(id: str, profile_id: int = None) -> Union[PostgrestAPIResponse | None, PostgrestAPIError | None]:
    try:
        results = GeneralService(table_name=table_name, profile_id=profile_id).delete_by_id(id=id)
    except PostgrestAPIError as e:
        return[ None, e.json()]
    return [results, None]

