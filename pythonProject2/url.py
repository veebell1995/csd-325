from django.url import path
from . import django

urlpatterns = [
    path("", django.home, name="home")
]