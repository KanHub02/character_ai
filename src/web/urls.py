from django.urls import path

from .views import (
    AmplitudeGenericView,
    TelegramUserCreateGeneric,
    TelegramUserCharacterSetView,
    CharacterListGeneric,
)


urlpatterns = [
    path(
        "v1/send-amplitude-event/",
        AmplitudeGenericView.as_view(),
        name="send-amplitude-event",
    ),
    path(
        "v1/create-telegram-user/",
        TelegramUserCreateGeneric.as_view(),
        name="create-telegram-user",
    ),
    path(
        "v1/telegram-user/set-character/",
        TelegramUserCharacterSetView.as_view(),
        name="telegram-user-set-character",
    ),
    path("v1/character-list/", CharacterListGeneric.as_view(), name="character-list"),
]
