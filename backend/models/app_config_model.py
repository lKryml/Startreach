from enum import Enum
from pydantic import BaseModel, Field
from typing import List, Union, Annotated

class EnviromentModel(str, Enum):
    development: str = 'development'
    production: str = 'production'
    test: str = 'test'

class AppConfigModel(BaseModel):
    port: Annotated[int, Field(ge=999)] = 1337
    app_name: str
    app_description: str
    app_version: Annotated[str, Field(min_length=1)] = '1.0.0'
    is_debug: bool
    enviroment: Annotated[EnviromentModel, Field(min_length=1)] = 'production'
    jwt_expires: int = 30
    jwt_refresh: int = 15
    jwt_secret: str = 'secret_key'
    jwt_algorithm: str = 'HS256'
    
    upload_path: str = 'uploads'
    temp_path: str = 'uploads/temp'
    images_path: str = 'uploads/images'