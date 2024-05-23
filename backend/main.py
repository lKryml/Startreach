import contorllers
import uvicorn
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.cors import CORSMiddleware
from pydantic import ValidationError
# from fastapi.templating import Jinja2Templates
# from fastapi.responses import HTMLResponse
from utils.request_handler import throw_exception
from utils.logger import logger

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
    "https://yourdomain.com"
]

# Add CORSMiddleware to the app
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow requests from these origins
    allow_credentials=True,  # Allow cookies to be sent in cross-origin requests
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allow all headers
)



app.mount("/assets", StaticFiles(directory="assets"), name="assets")
app.add_middleware(GZipMiddleware, minimum_size=1000)
app.include_router(contorllers.users.router)
app.include_router(contorllers.auth.router)
app.include_router(contorllers.projects.router)

@app.get('/health')
def health():
    return { "status": "OK" }

@app.exception_handler(ValidationError)
async def catch_validation_exceptions_middleware(request, exc: ValidationError):
    return throw_exception(exc)

async def catch_exceptions_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as e:
        # you probably want some kind of logging here
        logger.error("From CatchException")
        logger.error(e)
        return throw_exception({ "message": "something went wrong" })
app.middleware('http')(catch_exceptions_middleware)
logger.info("Starting the server")
   
if __name__ == '__main__':
    uvicorn.run('app:main', host='0.0.0.0', port=8000)