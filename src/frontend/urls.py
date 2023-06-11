from django.urls import path

from frontend.views import CharacterListTemplateView


urlpatterns = [
    path("menu/", CharacterListTemplateView.as_view(), name="test-menu"),
]
