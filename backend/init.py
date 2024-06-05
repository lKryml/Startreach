import contorllers
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.gzip import GZipMiddleware
from fastapi.middleware.cors import CORSMiddleware
from utils.exceptions import initializeAppExceptions
from utils.docs_security import initializeDocsGuards

def initializeApp():
    app = FastAPI(
        # docs_url=None, redoc_url=None, openapi_url=None
    )
    origins = [
        "http://localhost",
        "http://localhost:8080",
        "https://boostsomethin.ly"
    ]

    # Add CORSMiddleware to the app
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,  # Allow requests from these origins
        allow_credentials=True,  # Allow cookies to be sent in cross-origin requests
        allow_methods=["*"],  # Allow all HTTP methods (GET, POST, PUT, DELETE, etc.)
        allow_headers=["*"],  # Allow all headers
    )



    app.mount("/", StaticFiles(directory="assets"), name="assets")
    app.mount("/images", StaticFiles(directory="uploads/images", check_dir=False), name="images")
    app.add_middleware(GZipMiddleware, minimum_size=1000)
    app.include_router(contorllers.users.router)
    app.include_router(contorllers.auth.router)
    app.include_router(contorllers.projects.router)
    app.include_router(contorllers.webinars.router)
    app.include_router(contorllers.posts.router)

    initializeAppExceptions(app=app)
    initializeDocsGuards(app=app, username='admin', password='whatisthepassword?')


    @app.get('/health')
    def health():
        return { "status": "OK" }

    # @app.exception_handler(ValidationError)
    # async def catch_validation_exceptions_middleware(request, exc: ValidationError):
    #     return throw_exception(exc)
    
    
    # @app.exception_handler(PostgrestAPIError)
    # async def catch_supabase_exceptions_middleware(request, exc: PostgrestAPIError):
    #     return throw_exception(exc.json())

    # async def catch_exceptions_middleware(request: Request, call_next):
    #     try:
    #         return await call_next(request)
    #     except Exception as e:
    #         # you probably want some kind of logging here
    #         logger.error("From CatchException")
    #         logger.error(e)
    #         return throw_exception({ "message": "something went wrong" })
    # app.middleware('http')(catch_exceptions_middleware)
    return app