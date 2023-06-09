from django.urls import path

from front.views import main_menu


urlpatterns = [path("main-menu/", main_menu, name="main-menu")]
