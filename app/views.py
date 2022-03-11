from rest_framework import generics
from .models import CarModel
from .serializer import CarSerializerAutheticated

# Create your views here.

class CarView(generics.ListAPIView):
    queryset= CarModel.objects.all()
    serializer_class= CarSerializerAutheticated
    

