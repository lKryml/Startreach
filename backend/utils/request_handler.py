from http import HTTPStatus
from fastapi.responses import JSONResponse
from utils.logger import logger



def response_json(data, statusCode=HTTPStatus.OK):
    response = { 
        "data": data.data,
        "statusCode": statusCode,
        "status": "OK", 
        "count": data.count
    }
    return JSONResponse(response, statusCode)


def throw_exception(
        errors,
        status_code=HTTPStatus.INTERNAL_SERVER_ERROR,
    ):
    logger.error(errors)
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