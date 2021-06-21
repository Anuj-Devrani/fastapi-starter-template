from pydantic import BaseSettings, Field, AnyHttpUrl, AnyUrl
from typing import Optional, List


class AppConfig(BaseSettings):
    DEBUG: bool = Field(False, env='DEBUG')
    PROJECT_NAME: str = Field('Fast API', env='PROJECT_NAME')
    ALLOWED_HOSTS: List[AnyHttpUrl] = Field(['*'], env='ALLOWED_HOSTS')
    SQLALCHEMY_DATABASE_URI: AnyUrl
    API_VERSION: str = "/api/v1"

    API_PREFIX = "/api"

    class Config:
        env_file: str = ".env"


app_config = AppConfig()
