from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config.settings import app_config
from app.apis.api import api_router

app = FastAPI(
    title=app_config.PROJECT_NAME,
    debug=app_config.DEBUG,
    openapi_url=f'{app_config.API_VERSION}/openapi.json'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=app_config.ALLOWED_HOSTS,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix=app_config.API_VERSION)