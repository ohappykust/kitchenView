from pydantic import AnyHttpUrl, field_validator
from pydantic_core.core_schema import FieldValidationInfo
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Config(BaseSettings):
    model_config = SettingsConfigDict(case_sensitive=True)

    # Common config
    PROJECT_NAME: str = "KitchenView"
    SECRET_KEY: str = "insecure_key_for_dev"
    BACKEND_CORS_ORIGINS: list[AnyHttpUrl] = ["http://localhost:3000"]

    @field_validator("BACKEND_CORS_ORIGINS", mode="before")  # noqa
    @classmethod
    def assemble_cors_origins(cls, value: str | list[str]) -> list[str] | str:
        if isinstance(value, str) and not value.startswith("["):
            return [i.strip() for i in value.split(",")]
        if isinstance(value, (list, str)):
            return value
        raise ValueError(value)

    # Users config
    USERS_MAX_COUNT: int = 5

    # Database config
    POSTGRES_HOST: str
    POSTGRES_PORT: int = 5432
    POSTGRES_DB: str
    POSTGRES_USER: str | None
    POSTGRES_PASSWORD: str | None
    POSTGRES_HTTP_URI: str | None = None

    @field_validator("POSTGRES_HTTP_URI", mode="before")  # noqa
    @classmethod
    def assemble_postgresql_connection(cls, value: str | None, values: FieldValidationInfo) -> str:
        if isinstance(value, str):
            return value
        return f"postgresql://{values.data.get('POSTGRES_USER')}" \
               f":{values.data.get('POSTGRES_PASSWORD')}" \
               f"@{values.data.get('POSTGRES_HOST')}" \
               f":{values.data.get('POSTGRES_PORT')}" \
               f"/{values.data.get('POSTGRES_DB')}"

    # Type of save images: local or s3
    STATIC_SAVE_TYPE: str = "local"


@lru_cache(maxsize=1)
def get_config() -> Config:
    return Config()
