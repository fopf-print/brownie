import asyncio
import logging

from rpi import settings
from rpi.services import printing_process
from rpi.repositories import http_quantum


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def main_worker():
    logger.info('Main woker started!')
    async for task in http_quantum.try_fetch_task():
        logger.info('waiting for task...')
        if task is None:
            # TODO: добавить алерт
            logger.info('task not found --> sleep')
            await asyncio.sleep(settings.main_worker_delay_sec)
            continue

        logger.info('got task: %s', str(task.model_dump()))
        success = await printing_process.process_printing_task(task)

        await http_quantum.set_task_complete(task.id, success, 'ну тип что-то сделали')
        logger.info('done!')
