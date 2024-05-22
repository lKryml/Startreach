from http import HTTPStatus
from pydantic import BaseModel
from fastapi.responses import JSONResponse
from utils.logger import logger



def response_json(data, statusCode=HTTPStatus.OK):
    print("Data Type: ",  type(data))
    if isinstance(data, BaseModel):
        data = data.model_dump()
    
    response = { 
        "data": data.data if "data" in data else data,
        "statusCode": statusCode,
        "status": "OK", 
        "count": data.count if "count" in data else None
    }
    return JSONResponse(response, statusCode)


def throw_exception(
        errors,
        status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
    ):
    return JSONResponse(
        status_code=status_code,
        content=errors,
        headers={"X-Error": "Bad Request"},
    )


'''
if you want to switch from int id to uuid or mongodb
then you change id check from here
return valid id or None
'''
def get_id_param(id):
    id = int(id) if str(id).isnumeric() else None
    return id