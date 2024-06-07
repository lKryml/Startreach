from http import HTTPStatus
from fastapi import Request, FastAPI
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from supabase import PostgrestAPIError
from utils.request_handler import throw_exception


def initializeAppExceptions(app: FastAPI):
    
    @app.exception_handler(StarletteHTTPException)
    async def custom_http_exception_handler(request: Request, exc: StarletteHTTPException):
        print("From Exceptions.py: customer_http: ",exc.detail)
        return throw_exception(exc.detail, status_code=exc.status_code)


    @app.exception_handler(RequestValidationError)
    async def custom_validation_exception_handler(request: Request, exc: RequestValidationError):
        print("From Exceptions.py: Validation: ",exc.errors()[0])
        return throw_exception(exc.errors()[0]['msg'], status_code=HTTPStatus.UNPROCESSABLE_ENTITY)


    @app.exception_handler(PostgrestAPIError)
    async def custom_general_exception_handler(request: Request, exc: PostgrestAPIError):
        print("From Exceptions.py: PostGresSql: ",exc.detail)
        return throw_exception(exc.details, status_code=HTTPStatus.INTERNAL_SERVER_ERROR)


    @app.exception_handler(Exception)
    async def custom_general_exception_handler(request: Request, exc: Exception):
        print("From Exceptions.py: General: ",exc)
        return throw_exception("An unexpected error occurred", status_code=HTTPStatus.INTERNAL_SERVER_ERROR)
        