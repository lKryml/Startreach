import contorllers
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.gzip import GZipMiddleware
from pydantic import ValidationError
# from fastapi.templating import Jinja2Templates
# from fastapi.responses import HTMLResponse
from utils.request_handler import throw_exception
from utils.logger import logger

app = FastAPI()


app.mount("/assets", StaticFiles(directory="assets"), name="assets")
app.add_middleware(GZipMiddleware, minimum_size=1000)
app.include_router(contorllers.users.router)

@app.exception_handler(ValidationError)
async def catch_validation_exceptions_middleware(request, exc: ValidationError):
    return throw_exception(exc.errors)

async def catch_exceptions_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as e:
        # you probably want some kind of logging here
        logger.error(e)
        return throw_exception({ "message": "something went wrong" })
app.middleware('http')(catch_exceptions_middleware)
logger.info("Starting the server")
   
