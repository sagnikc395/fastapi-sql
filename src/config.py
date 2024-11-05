## all our env variables.

from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    POSTGRES_DB: str 

    model_config = SettingsConfigDict(
        env_file='.env',
        extra="ignore"
    )

settings = Settings()

# print the config data as a dict
# print(settings.model_dump())
