from pydantic_settings import BaseSettings,SettingsConfigDict

class GlobalConfig(BaseSettings):
    BASE_API_URL: str
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

global_config = GlobalConfig()
