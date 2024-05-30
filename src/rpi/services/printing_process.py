from rpi.entities import web
from rpi.repositories import sys_printing


async def process_printing_task(task: web.PrintingTaskWeb) -> web.CompletionStatus:
    # TODO: сделать асинхронно
    # (или забить и переделать всё на синхронно)

    filepath: str = sys_printing.run_download_file(task.id)

    sys_printing.run_lp(filepath, task.parameters)

    sys_printing.finish_task(filepath)

    return web.CompletionStatus.success
