import asyncio
from asgiref.sync import async_to_sync

from django.shortcuts import render

from rest_framework import generics, response, views

from .serializers import (
    AmplitudeSerializer,
    CreateTelegramUserSerializer,
    CharacterListSerializer,
)

from web.services.amplitude import AmplitudeRequestService
from web.services.chat_gpt import GptRequestService
from web.services.telegram_user import TelegramUserService
from web.services.character import CharacterServices


class AmplitudeGenericView(generics.GenericAPIView):
    serializer_class = AmplitudeSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            send_event = loop.create_task(
                AmplitudeRequestService.send_event(
                    serializer.data["device_id"], serializer.data["event_type"]
                )
            )
            loop.run_until_complete(send_event)

            return response.Response(
                {
                    "message": "ok",
                    "detail": "Amplitude event create successfully",
                    "status_code": 201,
                },
            )
        return response.Response(
            {"message": "Bad request", "detail": serializer.errors, "status_code": 400}
        )


class TelegramUserCreateGeneric(generics.GenericAPIView):
    serializer_class = CreateTelegramUserSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid(raise_exception=True):
            data = TelegramUserService.create_telegram_user(**serializer.validated_data)
            return response.Response(data=data)
        return response.Response(
            {"message": "Bad request", "detail": serializer.errors, "status_code": 400}
        )


class TelegramUserCharacterSetView(views.APIView):
    def post(self, request):
        user_id = self.request.query_params.get("user_id")
        character_id = self.request.query_params.get("character_id")
        if user_id and character_id:
            reponse_data = TelegramUserService.set_tg_user_character(
                character_id=character_id, telegram_id=user_id
            )
            return response.Response(reponse_data)

        return response.Response(
            data={
                "message": "Bad request",
                "detail": "required query params missed",
                "status_code": 400,
            }
        )


class CharacterListGeneric(generics.ListAPIView):
    serializer_class = CharacterListSerializer

    def get_queryset(self):
        return CharacterServices.get_list(is_deleted=False)
