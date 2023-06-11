import typing

from rest_framework import serializers

from .models import TelegramUser, Character


class AmplitudeSerializer(serializers.Serializer):
    device_id = serializers.CharField(max_length=255)
    event_type = serializers.CharField(max_length=255)


class CreateTelegramUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelegramUser
        fields = ("user_id", "username", "name", "surname")


class CreateCharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ("title", "greeting_message")


class CharacterListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ("id", "title", "greeting_message", "short_description", "image")
