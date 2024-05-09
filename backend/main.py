from cgi import print_exception
import logging
from logging import Formatter
from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse
from utils.request_handler import response_json
import contorllers
import uvicorn

app = FastAPI()

async def catch_exceptions_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as e:
        # you probably want some kind of logging here
        print_exception(e)
        return response_json({"msg": e.args})
app.middleware('http')(catch_exceptions_middleware)
app.include_router(contorllers.users.router)


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=5555, reload=True)
   
