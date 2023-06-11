from django.db import models
from django.core.validators import FileExtensionValidator

from common.models import BaseModel


class Character(BaseModel):
    title = models.CharField(
        verbose_name="Имя персонажа", max_length=255, null=False, blank=False
    )
    greeting_message = models.TextField(
        verbose_name="Сообщение приветствие", null=False, blank=True
    )
    image = models.FileField(
        blank=False,
        null=False,
        verbose_name="Изображение",
        upload_to="web/character/%Y/%m/%d/",
        validators=[FileExtensionValidator(allowed_extensions=["png", "jpg", "jpeg"])],
    )
    short_description = models.CharField(
        max_length=255, verbose_name="Краткое описание", null=True, blank=True
    )

    class Meta:
        db_table = "character"
        verbose_name = "Персонаж"
        verbose_name_plural = "Персонажи"

    def __str__(self) -> str:
        return self.title


class TelegramUser(BaseModel):
    user_id = models.CharField(
        verbose_name="Telegram ID", null=False, blank=False, unique=True, max_length=255
    )
    username = models.CharField(
        verbose_name="Telegram username", null=False, blank=False, max_length=255
    )
    name = models.CharField(verbose_name="Имя", null=True, blank=True, max_length=255)
    surname = models.CharField(
        verbose_name="Фамилие", null=True, blank=True, max_length=255
    )
    character = models.ForeignKey(
        "backend.Character",
        related_name="tg_users",
        verbose_name="Персонаж",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
    )

    class Meta:
        db_table = "telegram_user"
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self) -> str:
        return self.username
