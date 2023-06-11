from typing import Dict, List

import asyncio
from asgiref.sync import async_to_sync

from celery import shared_task

from backend.services.amplitude import AmplitudeRequestService


@shared_task
def send_amplitude_event_task(
    device_id: str,
    event_type: str,
) -> None:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    send_event = loop.create_task(
        AmplitudeRequestService.send_event(device_id, event_type)
    )
    loop.run_until_complete(send_event)
