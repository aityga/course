from django.shortcuts import render
from .models import *


def index(request):
    n = News.objects.all()
    context = {
        "news": n
    }
    return render(request, template_name='news/index.html', context=context)
