from ._prod import Settings as ProdSettings

from pydantic import Field
from pydantic_settings import SettingsConfigDict


class Settings(ProdSettings):
    # все dev-настройки в переменных окружения будут иметь приставку DEV_
    # пример: DEV_QUANTUM_URL
    model_config = SettingsConfigDict(env_prefix='DEV_')

    quantum_url: str = Field(
        description="URL или IP-шник сервера quantum",
        default='http://127.0.0.1:8000',
    )
