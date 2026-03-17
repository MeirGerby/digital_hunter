
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    MYSQL_HOST: str 
    MYSQL_USER: str  
    MYSQL_PORT: int 
    MYSQL_PASSWORD: str 
    MYSQL_DATABASE: str 

    model_config = SettingsConfigDict(
        env_file='.env',
        extra='ignore'
    )

config = Settings()


