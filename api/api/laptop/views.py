from django.db.models import query
from rest_framework import generics, permissions
from .serializers import *
from .models import Laptop
from .permissions import *

class LaptopCreateView(generics.CreateAPIView):
    serializer_class = LaptopAllSerializers

class LaptopListView(generics.ListAPIView):
    serializer_class = LaptopAllSerializers
    queryset = Laptop.objects.all()

class LaptopDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = LaptopAllSerializers
    queryset = Laptop.objects.all()
    permission_classes = (IsOwnerOrReadOnly, )
