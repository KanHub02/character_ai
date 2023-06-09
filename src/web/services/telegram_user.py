from typing import ClassVar, List, Dict

from web.models import TelegramUser, Character


class TelegramUserService:
    __model__ = TelegramUser
    __model_character__ = Character

    @classmethod
    def create_telegram_user(cls, **validated_data: Dict) -> Dict[str, str]:
        exists = cls.__model__.objects.filter(
            user_id=validated_data.get("user_id")
        ).exists()
        if exists:
            return {
                "message": "Unique constraint",
                "detail": "User with this id already exists",
                "status_code": 200,
            }

        cls.__model__.objects.create(**validated_data).save()
        return {"message": "Ok", "detail": "User created", "status_code": 201}

    @classmethod
    def set_tg_user_character(cls, character_id: str, telegram_id: str) -> Dict:
        character = cls.__model_character__.objects.filter(id=character_id).first()
        if character:
            tg_user = cls.__model__.objects.filter(user_id=telegram_id).first()
            tg_user.character = character
            tg_user.save()
            return {
                "message": "Ok",
                "detail": "User character updated",
                "status_code": 204,
            }

        return {
            "message": "Object not found",
            "detail": "Character with this id not found",
            "status_code": 200,
        }
