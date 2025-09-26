from pydantic_settings import BaseSettings,SettingsConfigDict

class CommissionConfig(BaseSettings):
    GET_DISTRICT_COMMISSION_BY_COMMISSION_ID: str
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", extra="ignore")

commission_config = CommissionConfig()
