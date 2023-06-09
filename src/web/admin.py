from django.contrib import admin

from web.models import Character, TelegramUser

admin.site.register(Character)
admin.site.register(TelegramUser)
