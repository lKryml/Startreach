from typing import Annotated, Union, List
from pydantic import BaseModel, Field, constr


class PaginationModel(BaseModel):
    page: Annotated[int, Field(ge=1)] = 1
    per_page: Annotated[int, Field(ge=10, le=100)] = 10
    sort_order: Annotated[str | None, Field(pattern=r"asc|desc")] = 'asc'
    sort_by: str | None = 'id',
    fields: List[str] | str = '*'
