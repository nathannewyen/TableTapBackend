import os
from pydantic_settings import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):
    DATABASE_URL: str
    APP_NAME: str = "Restaurant Food Ordering API"
    DEBUG: bool = True
    
    # AWS S3 Configuration
    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    AWS_REGION: str = "us-east-1"
    AWS_S3_BUCKET: str
    AWS_S3_BASE_URL: str

    class Config:
        env_file = ".env"

@lru_cache()
def get_settings():
    return Settings()