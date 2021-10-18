from django.urls import path
from .views import addnew, index, edit, update, delete

urlpatterns = [
    path('', index),
    path('addnew', addnew),
    path('edit/<int:id>', edit),  
    path('update/<int:id>', update),  
    path('delete/<int:id>', delete),  
]