from django.shortcuts import render


def main_menu(request):
    return render(request, "index.html")


# Create your views here.
