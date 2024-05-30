from typing import AsyncIterable
from uuid import UUID
from urllib.parse import urljoin

from aiohttp import ClientSession

from rpi import settings
from rpi.entities import web


async def try_fetch_task() -> AsyncIterable[web.PrintingTaskWeb | None]:
    while True:
        async with ClientSession() as session:
            async with session.get(
                urljoin(settings.quantum_url, '/try-get-task'),
                params={'printer_id': settings.printer_id},
            ) as resp:
                if resp.status != 200:
                    # TODO: сделать алерт
                    # за сон отвечает caller
                    yield None
                elif (data := (await resp.json())['task']) is None:
                    # TODO: сделать алерт
                    # за сон отвечает caller
                    yield None
                else:
                    yield web.PrintingTaskWeb.model_validate(data)


async def set_task_complete(task_id: UUID, status: web.CompletionStatus, comment: str) -> None:
    async with ClientSession() as session:
        async with session.post(
            urljoin(settings.quantum_url, '/set-task-printing-complete/'),
            json={
                'task_id': str(task_id),
                'status': status,
                'comment': comment,
            },
        ) as resp:
            if resp.status != 200:
                raise RuntimeError('wtf?')
