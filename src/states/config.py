from pydantic_settings import BaseSettings,SettingsConfigDict

class StateConfig(BaseSettings):
    GET_ALL_STATE_URL: str
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

state_config = StateConfig()
