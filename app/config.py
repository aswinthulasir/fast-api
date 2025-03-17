from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

class Settings(BaseSettings):
    database_hostname: str = os.getenv("DATABASE_HOSTNAME")
    database_port: str = os.getenv("DATABASE_PORT")
    database_name: str = os.getenv("DATABASE_NAME")
    database_username: str = os.getenv("DATABASE_USERNAME")
    database_password: str = os.getenv("DATABASE_PASSWORD")
    secret_key: str = os.getenv("SECRET_KEY")
    algorithm: str = os.getenv("ALGORITHM")
    access_token_expire_minutes: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

settings = Settings()
