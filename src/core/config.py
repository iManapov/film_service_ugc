import os
from logging import config as logging_config


from pydantic import BaseSettings






class Settings(BaseSettings):
    """Конфиг сервиса"""

    authjwt_secret_key: str = "super-secret" # должен совпадать с сервисом авторизации



settings = Settings()
