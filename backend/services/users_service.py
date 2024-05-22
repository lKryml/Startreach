from supabase import PostgrestAPIResponse, PostgrestAPIError
from .general_service import GeneralService
from models import UserModel, PaginationModel
from db import supabase
from typing import List, Union

table_name = 'users'

def user_exists(key: str = "email", value: str = None, id = None) -> bool:
    query = supabase.table(table_name=table_name).select("*").eq(key, value)
    if id:
        query = query.not_eq("id", id)
    user_count = query.limit(1).execute()
    return True if len(user_count.data) != 0 else False


def create_user(user: UserModel, is_login: bool = False) -> Union[PostgrestAPIResponse | None, Exception | PostgrestAPIError | None]:
    user_email = user.email.lower()
    # TODO implement hashing for password
    # hashed_password = bcrypt.hashpw(user.password.encode(), bcrypt.gensalt())
    # print(hashed_password.decode('utf-8'))
    if user_exists(key='email', value=user_email):
        return [None, {"message": "User already exists"}]
    [user, err] = GeneralService(table_name=table_name).create(user.model_dump())
    # if err is None and is_login:
    #     print(login({'email': user.email, 'password': user.password }))
    return [user, err]



def get_user(id: Union[PostgrestAPIResponse, None] = None):
    return GeneralService(table_name=table_name).find_by_id(id=id)

def get_users(pagination: PaginationModel) -> Union[PostgrestAPIResponse | None, PostgrestAPIError | None]:
    return GeneralService(table_name=table_name).find(pagination=pagination, model=UserModel, search_dict={})

def get_last_user_id():
    try:
        user = supabase.table(table_name=table_name).select("id").order("id", desc=True).limit(1).execute()
    except PostgrestAPIError as err:
        return [None, err.json()]
    if len(user.data) == 0:
        return [0, None]
    return [user.data[0]['id'], None]    


def update_user(id: str, item: dict):
    # if user_exists(key='email', value=item.email, id=id):
    #     return [None, PostgrestAPIError({"message": "Email already exists"}).json()]
    try:
        user = (
            supabase.table(table_name=table_name)
            .update(item)
            .eq("id", id)
            .execute()
        )
    except PostgrestAPIError as e:
        return[ None, e.json()]
    return [user, None]


def delete_user(id: str) -> Union[PostgrestAPIResponse | None, PostgrestAPIError | None]:
    try:
        results = GeneralService(table_name=table_name).delete_by_id(id=id)
    except PostgrestAPIError as e:
        return[ None, e.json()]
    return [results, None]        

