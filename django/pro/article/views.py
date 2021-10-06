from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(requests):
    return HttpResponse("Hello world")


def index2(requests):
    return HttpResponse("Hello world2")


def index3(requests):
    return HttpResponse("Hello world3")
