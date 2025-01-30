from pydantic_settings import BaseSettings
from typing import List  # ✅ Import List from typing

class Settings(BaseSettings):

    APP_NAME: str
    APP_VERSION: str

    FILE_ALLPWED_EXTENSTIONS:list
    FILE_ALLPWED_SIZE :int 
    class Config:
        env_file = ".env"
def get_settings():
    return Settings()  # ✅ Make sure this function is defined!