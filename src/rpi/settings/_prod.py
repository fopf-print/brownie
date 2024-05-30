from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    printer_id: int = Field(
        description='айдишник принтера',
        default=0,  # нулевой айдишник является айдишником тестового принтера
    )
    main_worker_delay_sec: int = Field(
        description='пауза в работе главного воркера',
        default=10,
    )
    path_to_tmp: str = Field(
        description='путь до временной папки для сохранения всякого',
        default='/tmp',
    )
    cups_printer_name: str = Field(
        description='имя принтера для запуска `lp<smth> -d _вот_тут_оно_` команд',
        # TODO: тянуть только из окружения
        default='HP_LaserJet_M14-M17',
    )
    quantum_url: str = Field(
        description="URL или IP-шник сервера quantum",
        default='http://example.com/',
    )
