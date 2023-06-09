from typing import Dict, ClassVar

from web.models import Character


class CharacterServices:
    __model__ = Character

    @classmethod
    def get_list(cls, **kwargs):
        return (
            cls.__model__.objects.filter(**kwargs)
            .order_by("-created_at")
            .only("id", "title", "greeting_message", "short_description", "image")
        )
