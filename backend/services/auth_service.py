from fastapi import Request
from pydantic import ValidationError
from core.config import app_config
from models import AuthModel, UserModel, TokenModel, UserAuthenticatedModel
from supabase import PostgrestAPIError
from db import supabase
from .users_service import user_exists
from .general_service import GeneralService
import datetime
from jose import jwt, JWTError

table_name = 'users'
token_table_name = 'tokens'

def login(credentials: AuthModel):
    user_data = supabase.table(table_name=table_name).select('*').eq('email', credentials.email).limit(1).execute()
    if 0 == user_data.data.count or user_data.data[0]['password'] != hash_pass(credentials.password):
        return [None, PostgrestAPIError({"message": "user not found"}).json()]
    user = UserModel(**user_data.data[0])
    expires_at = datetime.datetime.utcnow() + datetime.timedelta(seconds=60 * int(app_config.get('jwt_expires')))
    expires_at_format = expires_at.isoformat()
    jwt_encoded = encode_jwt(user.id, expires_at=expires_at)
    try:
        token = TokenModel(
            token=jwt_encoded,
            sub=user.id,
            expires=expires_at_format,
            blocked=False
        )
    except ValidationError as e:
        return [None, e.json()]
    t = supabase.table(table_name=token_table_name).insert(token.model_dump()).execute()
    print(decode_jwt(str(jwt_encoded)))
    user_dict = user.model_dump()
    user_dict['access_token'] = jwt_encoded
    user_dict['refresh_token'] = jwt_encoded
    user_with_token = UserAuthenticatedModel(**user_dict)
    print("User From AuthServiec", user_with_token)
    return [user_with_token.model_dump(), None]


def register(data: AuthModel):
    if user_exists(key='email', value=data.email):
        return [None, {"message": "User already exists"}]
    
    user_dict = data.model_dump()
    user_dict['profile_id'] = 1
    try:
        user = UserModel(
            email=user_dict['email'], 
            password=hash_pass(user_dict['password']), 
            profile_id=1,
            user_type=1
        )
    except ValidationError as e:
        return [None, e.json()]
    [user, err] = GeneralService(table_name=table_name).create(user.model_dump(exclude=['id']))
    
    return  [user, err]

def hash_pass(password: str):
    return password

def encode_jwt(user_id: str, expires_at: datetime.datetime):
    secret = app_config.get('jwt_secret')
    alogo = app_config.get('jwt_algorithm')
    expires_at = datetime.datetime.utcnow() + datetime.timedelta(seconds=60 * int(app_config.get('jwt_expires')))
    refresh_expires_at = datetime.datetime.utcnow() + datetime.timedelta(seconds=60 * int(app_config.get('jwt_refresh')))
    return jwt.encode({
        "sub": user_id,
        "exp": expires_at.timestamp(),
        "iat": refresh_expires_at.timestamp(),
    }, secret, algorithm="HS256")
    
def decode_jwt(token):
    secret = app_config.get('jwt_secret')
    alogo = app_config.get('jwt_algorithm')
    print("--------------------------------")
    print(secret, alogo, token)
    print("--------------------------------")
    try:
        jwt.decode(token, secret, algorithms=["HS256"])
    except JWTError as e:
        print(e)
    return None

async def auth_protecter(req: Request):
    jwt_encoded = req.headers.get('Authorization')
    print(jwt_encoded)
    
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
    
    
    
    