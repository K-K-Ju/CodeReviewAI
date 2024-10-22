import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv(dotenv_path='./.env')


class Settings(BaseSettings):
    openai_api_key: str
    github_api_key: str


settings = Settings()
