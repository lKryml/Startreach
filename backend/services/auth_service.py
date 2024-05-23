from utils.logger import logger
from fastapi import Request
from pydantic import ValidationError
from models import AuthModel, UserModel, UserAuthenticatedModel, ProfileModel
from supabase import PostgrestAPIError
from db import supabase
from .tokens_service import create_token
from .users_service import user_exists, get_user, update_user
from .general_service import GeneralService
from .profile_service import create_profile 

table_name = 'users'
token_table_name = 'tokens'
profile_table_name = 'profile'

def login(credentials: AuthModel):
    user_data = supabase.table(table_name=table_name).select('*, profiles(*)').eq('email', credentials.email).limit(1).execute()
    if 0 == user_data.data.count or user_data.data[0]['password'] != hash_pass(credentials.password):
        return [None, PostgrestAPIError({"message": "user not found"}).json()]
    user_dict = user_data.data[0]
    user_id = user_dict['id']
    del user_dict['id']
    user = UserModel(**user_dict)
    [token, err] = create_token(user_id)
    user_dict = user.model_dump()
    user_dict['id'] = user_id
    user_dict['access_token'] = token.data[0]['token']
    user_dict['refresh_token'] = token.data[0]['token']
    user_with_token = UserAuthenticatedModel(**user_dict)
    return [user_with_token.model_dump(), None]


def register(data: AuthModel, body: Request.body):
    if user_exists(key='email', value=data.email):
        return [None, {"message": "User already exists"}]
    
    user_dict = data.model_dump()
    try:
        user = UserModel(
            email=user_dict['email'], 
            password=hash_pass(user_dict['password']), 
            user_type=1,
            profile_id=0
        )
    except ValidationError as e:
        return [None, e.json()]
    [user, err] = GeneralService(table_name=table_name).create(user.model_dump(exclude=['id', 'profile_id', 'profile']))
    if err is not None:
        return [None, err]
    
    
    [token, err] = create_token(user.data[0]['id'])
    user_dict = user.data[0]
    user_dict['access_token'] = token.data[0]['token']
    user_dict['refresh_token'] = token.data[0]['token']
    user_with_token = UserAuthenticatedModel(**user_dict)
    print("user_with_token: ", user_with_token.model_dump())
    return [user_with_token.model_dump(), None]


def complete_registration(user_id: int, profile: ProfileModel):
    [user, err] = get_user(profile.user_id)
    if user is None:
        return [None, err.json()]

    [new_profile, err] = create_profile(profile)
    print(new_profile.data[0], "is New Profile")

    if new_profile is None:
        return [None, err.json()]
    
    [user_updated, err] = update_user(id=user_id, item={ 
        "user_type": profile.profile_type, 
        "profile_id": new_profile.data[0]["id"],
    })
    
    return [new_profile.data[0], None]


def hash_pass(password: str):
    return password

async def auth_protecter(req: Request):
    jwt_encoded = req.headers.get('Authorization')

    # try:
    #     jwt_decoded = decode_jwt(token)
    #     user_id = jwt_decoded.get('sub')
    # except JWTError as e:
    #     return None
    user_id = 9 # for testing 
    # token = supabase.table(table_name=token_table_name).select('*').eq('token', jwt_encoded).limit(1).execute()
    token = supabase.table(table_name=token_table_name).select('*').eq('sub', user_id).limit(1).execute()
    if len(token.data) == 0: # or token.user_id != user_id:
        return None
    # print(jwt_decoded)
    try:
        user = supabase.table(table_name=table_name).select('*').eq('id', user_id).execute()
        return UserModel(**user.data[0])
    except PostgrestAPIError as e:
        return None
    
def logout(user: UserModel):
    try:
        # all user tokens
        # results = supabase.table(table_name=token_table_name).delete().eq('sub', user.user_id).execute()    
        # or by the token he signed in with or something
        results = supabase.table(table_name=token_table_name).delete().eq('token', user.access_token).execute()    
    except PostgrestAPIError as e:
        return [None, e.json()]
    return [results, None]
