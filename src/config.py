import os
from functools import lru_cache

from settings.base import Settings


@lru_cache()
def get_settings(env_name: str = None) -> Settings:
    """Getting environment settings"""
    env_name = env_name or os.getenv("APP_ENV", "")
    env_file = f".env.{env_name}" if env_name else Settings.Config.env_file

    return Settings(_env_file=env_file)
