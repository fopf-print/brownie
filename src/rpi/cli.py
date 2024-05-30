import asyncio
import click


@click.group()
def cli():
    pass


@cli.command()
def run_worker():
    from rpi.services.workers import main_worker
    asyncio.get_event_loop().run_until_complete(main_worker())
