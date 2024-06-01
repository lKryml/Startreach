import datetime
from typing import List, Union, Any, Annotated, Optional
from pydantic import BaseModel, Field

class PostsModel(BaseModel):
    title: str
    post: Annotated[str | None, Field(min_length=2)] = None
    category_id: Annotated[int | None, Field(min=1)] = None
    user_id: Annotated[int | None, Field(min=0)] = None
    profile_id: Annotated[int | None, Field(min=0)] = None
    tags: list[str] | None = None
    createdAt: datetime.datetime | None = None
    is_active: bool = True
    img: Annotated[str | None, Field(min_length=4)] = None