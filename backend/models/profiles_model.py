from typing import List, Union, Annotated, Optional
from pydantic import BaseModel, Field
from .global_model import LocationModel


class ProfileModel(BaseModel):
    name: str
    profile_type: Annotated[int, Field(min=2)]
    email: Annotated[str | None, Field(min_length=2)] = None
    avatar: Annotated[str | None, Field(min_length=2)] = None
    description: Annotated[str | None, Field(min_length=2)] = None
    phone: Annotated[str | None, Field(min_length=2)] = None
    bio: Annotated[str | None, Field(min_length=2)] = None
    city: Annotated[str | None, Field(min_length=2)] = None
    category_id: Annotated[int | None, Field(min=1)] = None
    user_id: Annotated[int, Field(min=0)]

class ProfileInfoModel(BaseModel):
    location: LocationModel
    profile_id: Annotated[int, Field(min=1)]
    employees_count: Annotated[int | None, Field(min=1)] = None
    since: int
    img: str
# export interface IProfile {
#     id: number,
#     phones: string[], // [09283232323, 094334234234432423234]
#     name: string,
#     email: string,
#     avatar: string,
#     bio: string,
#     address: string,
#     type: UsersTypes,
#     user_id: number,
#     created_at: string,
#     info: IProfileInfo
# }

# export interface IProfileInfo {
#     since: Date,
#     location: {
#         lang: number,
#         lat: number
#     },
#     img: string, // for profile background
#     profile_id: IProfile['id'],
#     employees_count: number,
# }