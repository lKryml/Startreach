from pydantic import ValidationError
from core.config import app_config
from models import TokenModel
from supabase import PostgrestAPIError
from db import supabase
import datetime
from jose import jwt, JWTError

token_table = 'tokens'

def create_token(user_id):
    expires_at = datetime.datetime.utcnow() + datetime.timedelta(seconds=60 * int(app_config.get('jwt_expires')))
    expires_at_format = expires_at.isoformat()
    jwt_encoded = encode_jwt(user_id, expires_at=expires_at)
    try:
        token = TokenModel(
            token=jwt_encoded,
            sub=user_id,
            expires=expires_at_format,
            blocked=False
        )
    except ValidationError as e:
        return [None, e.json()]
    try:
        new_token = supabase.table(table_name=token_table).insert(token.model_dump()).execute()
    except PostgrestAPIError as e:
        return [None, e.json()]
    return [new_token, None]
    

def encode_jwt(user_id: str, expires_at: datetime.datetime):
    secret = app_config.get('jwt_secret')
    algo = app_config.get('jwt_algorithm')
    expires_at = datetime.datetime.utcnow() + datetime.timedelta(seconds=60 * int(app_config.get('jwt_expires')))
    refresh_expires_at = datetime.datetime.utcnow() + datetime.timedelta(seconds=60 * int(app_config.get('jwt_refresh')))
    return jwt.encode({
        "sub": str(user_id),
        "exp": expires_at.timestamp(),
        "iat": refresh_expires_at.timestamp(),
    }, secret, algorithm=algo)

def decode_jwt(token):
    secret = app_config.get('jwt_secret')
    algo = app_config.get('jwt_algorithm')
    try:
        decoded_jwt = jwt.decode(token, secret , algorithms=[algo])
        return decoded_jwt
    except JWTError as e:
        print(e)
        raise JWTError(e)