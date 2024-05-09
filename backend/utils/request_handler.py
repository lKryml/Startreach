from http import HTTPStatus
from fastapi.responses import JSONResponse




def response_json(data, statusCode=HTTPStatus.OK):
    response = { 
        "data": data,
        "statusCode": statusCode,
        "status": "OK", 
    }
    if len(data) > 0:
        response['count'] = len(data)
    return JSONResponse(response, statusCode)


def throw_exception(
        errors,
        status_code=HTTPStatus.UNPROCESSABLE_ENTITY,
    ):
    return JSONResponse(
        status_code=status_code,
        content=errors,
        headers={"X-Error": "Bad Request"},
    )