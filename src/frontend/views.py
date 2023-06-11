from typing import Any
from urllib.parse import urlencode

from django.shortcuts import render
from django.views.generic import ListView
from django.db.models import QuerySet
from django.urls import reverse

from backend.services.character import CharacterServices


class CharacterListTemplateView(ListView):
    template_name = "index.html"

    def get_queryset(self) -> QuerySet[Any]:
        return CharacterServices.get_list(is_deleted=False)


# Create your views here.
