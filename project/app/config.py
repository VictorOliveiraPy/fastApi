import logging
import os
from functools import lru_cache

from pydantic import BaseSettings, AnyUrl

log = logging.getLogger('uvicorn')

""" environment - define o ambiente (ou seja, dev, stage, prod)
    testing - define se estamos ou não em modo de teste
"""


class Settings(BaseSettings):
    environment: str = os.getenv("ENVIRONMENT", "dev")
    testing: bool = os.getenv("TESTING", 0)
    database_url: AnyUrl = os.environ.get("DATABASE_URL")


@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the enviroment...")
    return Settings()
