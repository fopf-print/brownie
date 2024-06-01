import os
from typing import Any
from urllib.parse import urljoin, urlencode
from uuid import UUID

from rpi import settings
from rpi.entities import web


def _execute(cmd: str, *args: Any) -> int:
    # да, это костыль вместо os.execlp (or smth)
    # но мне лень делать fork)
    args_combined = ' '.join(f"'{arg}'" for arg in args)
    full_command = f'{cmd} {args_combined}'
    return os.system(full_command)


def run_download_file(task_id: UUID, filename: str | None = None) -> str:
    filename = filename or f'{task_id}.pdf'

    # TODO: переделать на `.../download-file/f981f359-04d5-4f6c-8d6b-023c0f3478f1`
    url_with_params: str = (
        urljoin(settings.quantum_url, '/download-file') + '?' + urlencode({'printing_task_id': str(task_id)})
    )

    filepath: str = os.path.join(settings.path_to_tmp, filename)
    if _execute('wget', url_with_params, '-O', filepath) != 0:
        # TODO: придумать что-нибудь
        # да похуй)
        # raise RuntimeError('smth wrong')
        pass

    return filepath


def run_lp(filepath: str, params: web.PrintingParameters) -> None:
    _ = params  # unused, но пока похуй
    _execute('lp', '-d', settings.cups_printer_name, filepath)


def finish_task(filepath: str) -> None:
    _execute('rm', '-f', filepath)
