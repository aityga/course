from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    context = {
        'mood': ['klass', 'norm', 'ujas']
    }
    return render(request, 'articles/index.html', context=context)


def index2(request):
    return render(request, 'articles/index2.html')
#
#
def index3(request):
    return HttpResponse('hi')


# def index4(request):
#     return render(request, 'articles/index4.html')
#
#
# def index5(request):
#     return render(request, 'articles/index5.html')
#
#
# def index6(request):
#     return render(request, 'articles/index6.html')
