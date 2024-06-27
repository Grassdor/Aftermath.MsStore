"""Base settings"""

from pydantic import BaseModel, PostgresDsn, field_validator
from pydantic_settings import BaseSettings


class PostgresSettings(BaseModel):
    """PostgreSQL settings."""

    dsn: PostgresDsn
    host: str
    port: int
    name: str
    user: str
    password: str

    @field_validator('dsn')
    def validate_dsn(cls, value: PostgresDsn) -> PostgresDsn:
        """Check DSN async option."""

        if 'asyncpg' not in value.scheme:
            raise ValueError('You should to use asyncpg option in DSN scheme')

        return value


class Settings(BaseSettings):
    """Application settings."""

    postgres: PostgresSettings
    debug: bool = False
    origins: list = ['*']

    class Config:
        env_file = '.env'
        env_nested_delimiter = '__'
