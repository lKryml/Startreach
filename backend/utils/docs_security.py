from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.openapi.docs import get_swagger_ui_html, get_redoc_html
from utils.logger import logger
import secrets

def initializeDocsGuards(app: FastAPI, username: str, password: str):
    security = HTTPBasic()

    def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
        print(f"Received credentials: {credentials.username}, {credentials.password}")
        logger.info(f"Received credentials: {credentials.username}, {credentials.password}")
        correct_username = secrets.compare_digest(credentials.username, username)
        correct_password = secrets.compare_digest(credentials.password, password)
        if not (correct_username and correct_password):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Basic"},
            )
        return credentials.username

    @app.get("/docs", include_in_schema=False)
    async def get_docs(current_user: str = Depends(get_current_username)):
        return get_swagger_ui_html(openapi_url="/openapi.json", title=app.title + " - Swagger UI")

    @app.get("/redoc", include_in_schema=False)
    async def get_redoc(current_user: str = Depends(get_current_username)):
        return get_redoc_html(openapi_url="/openapi.json", title=app.title + " - ReDoc")

    @app.get("/openapi.json", include_in_schema=False)
    async def get_openapi(current_user: str = Depends(get_current_username)):
        return app.openapi()
