from pydantic import BaseSettings
import os


class Settings(BaseSettings):
    MODE: str
    
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @property
    def DB_URL(self):
        return f"postgresql+psycopg2://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    class Config:
        env_file = ".env" if os.environ.get("MODE") != "TEST" else ".env-test"


settings = Settings()
