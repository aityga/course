from django.urls import path
from .views import addnew, index

urlpatterns = [
    path('', index),
    path('addnew', addnew)
]