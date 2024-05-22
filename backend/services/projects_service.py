from supabase import PostgrestAPIResponse, PostgrestAPIError
from .general_service import GeneralService
from models import ProjectsModel, PaginationModel
from db import supabase
from typing import List, Union

table_name = 'projects'

def project_exists(key: str = "email", value: str = None, id = None) -> bool:
    query = supabase.table(table_name=table_name).select("*").eq(key, value)
    if id:
        query = query.not_eq("id", id)
    project_count = query.limit(1).execute()
    return True if len(project_count.data) != 0 else False


def create_project(project: ProjectsModel):
    
    project_json = project.model_dump(exclude=['createdAt', 'id'])
    project_json['launch_date'] = project.launch_date.date().isoformat()
    [project, err] = GeneralService(table_name=table_name).create(project_json)
    if err is not None:
        print("Error: From Project Service", err)
    return [project, err]

def get_last_project_id():
    try:
        project = supabase.table(table_name=table_name).select("id").order("id", desc=True).limit(1).execute()
    except PostgrestAPIError as err:
        return [None, err.json()]
    if len(project.data) == 0:
        return [0, None]
    return [project.data[0]['id'], None]
    

def get_project(id: Union[PostgrestAPIResponse, None] = None):
    return GeneralService(table_name=table_name).find_by_id(id=id)

def get_projects(pagination: PaginationModel) -> Union[PostgrestAPIResponse | None, PostgrestAPIError | None]:
    return GeneralService(table_name=table_name).find(pagination=pagination, model=ProjectsModel, search_dict={})
    


def update_project(id: str, item):
    try:
        project = (
            supabase.table(table_name=table_name)
            .update(item)
            .eq("id", id)
            .execute()
        )
    except PostgrestAPIError as e:
        return[ None, e.json()]
    return [project, None]


def delete_project(id: str) -> Union[PostgrestAPIResponse | None, PostgrestAPIError | None]:
    try:
        results = GeneralService(table_name=table_name).delete_by_id(id=id)
    except PostgrestAPIError as e:
        return[ None, e.json()]
    return [results, None]        

