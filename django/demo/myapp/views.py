from django.shortcuts import HttpResponse

# Create your views here.


def home():
    return HttpResponse("bell says hello")