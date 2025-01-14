import logging
from celery import shared_task
from django.core.management import call_command
from .management.commands.send_to_opc import Command as SendToOpcCommand


logger = logging.getLogger('filling_station')

# @shared_task
# def send_to_opc(reader, blink):
#     logger.info('таска send_to_opc выполняется...')
#     command = SendToOpcCommand()
#     command.handle(reader=reader, blink=blink)

@shared_task
def send_to_opc(reader, blink):
    logger.info('таска send_to_opc выполняется...')
    call_command('send_to_opc', reader=reader, blink=blink)
