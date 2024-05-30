# при импорте settings модуль заменяется на класс
# но хочется иметь подсказки и нематерящийся mypy

# поэтому поля классов Settings перечислены тут

printer_id: int
quantum_url: str
path_to_tmp: str
cups_printer_name: str
main_worker_delay_sec: int

__all__ = [
    'printer_id',
    'quantum_url',
    'main_worker_delay_sec',
]
