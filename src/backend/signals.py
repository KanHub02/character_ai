import asyncio

from django.db.models.signals import pre_save
from django.dispatch import receiver

from backend.models import Character
from backend.services.chat_gpt import GptRequestService


@receiver(pre_save, sender=Character)
def create_character(sender, instance, **kwargs):
    if not instance.greeting_message:
        data = GptRequestService(instance.title)
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        send_event = loop.create_task(data.create_character(instance))
        loop.run_until_complete(send_event)
