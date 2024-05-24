from supabase import PostgrestAPIResponse, PostgrestAPIError
from .general_service import GeneralService
from models import ProfileModel, ProfileInfoModel, PaginationModel
from db import supabase
from typing import List, Union

table_name = 'profiles'

def profile_exists(key: str = "email", value: str = None, id = None) -> bool:
    query = supabase.table(table_name=table_name).select("*").eq(key, value)
    if id:
        query = query.not_eq("id", id)
    profile_count = query.limit(1).execute()
    return True if len(profile_count.data) != 0 else False


def create_profile(profile: ProfileModel):
    [profile, err] = GeneralService(table_name=table_name).create(profile.model_dump())
    if err is not None:
        print(err)
    return [profile, err]

def get_last_profile_id():
    try:
        profile = supabase.table(table_name=table_name).select("id").order("id", desc=True).limit(1).execute()
    except PostgrestAPIError as err:
        return [None, err.json()]
    if len(profile.data) == 0:
        return [0, None]
    return [profile.data[0]['id'], None]
    

def get_profile(id: Union[PostgrestAPIResponse, None] = None):
    return GeneralService(table_name=table_name).find_by_id(id=id)

def get_profiles(pagination: PaginationModel) -> Union[PostgrestAPIResponse | None, PostgrestAPIError | None]:
    return GeneralService(table_name=table_name).find(pagination=pagination, model=ProfileModel)
    


def update_profile(id: str, item):
    try:
        profile = (
            supabase.table(table_name=table_name)
            .update(item)
            .eq("id", id)
            .execute()
        )
    except PostgrestAPIError as e:
        return[ None, e.json()]
    return [profile, None]


def delete_profile(id: str) -> Union[PostgrestAPIResponse | None, PostgrestAPIError | None]:
    try:
        results = GeneralService(table_name=table_name).delete_by_id(id=id)
    except PostgrestAPIError as e:
        return[ None, e.json()]
    return [results, None]        

