from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class PostgresConfig(BaseModel):
    user: str
    password: str
    name: str
    host: str = "localhost"
    port: int = 5432

    @property
    def asyncpg_url(self) -> str:
        return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        extra="ignore",
        env_file=".env",
        env_nested_delimiter="__",
    )

    postgres: PostgresConfig


settings = Settings()
