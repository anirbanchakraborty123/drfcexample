from rest_framework import generics
from .models import CarModel
from .serializer import CarSerializer, UnAuthorizedCarSerializer

class CarView(generics.ListAPIView):
    queryset = CarModel.objects.all()
    serializer_class = CarSerializer
    serializer_anonymous_class = UnAuthorizedCarSerializer
    
    def get_serializer_class(self):

        if not self.request.user.is_authenticated:
            return self.serializer_anonymous_class

        return super().get_serializer_class()