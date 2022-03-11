from rest_framework import generics
from .models import CarModel, Engine
from .serializer import CarSerializerAutheticated,CarmodelengineSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny,BasePermission,IsAuthenticatedOrReadOnly
from django.contrib.auth.models import AnonymousUser

# Create your views here.

class CarView(generics.ListAPIView):
    queryset= CarModel.objects.all()
    serializer_class= CarSerializerAutheticated

    def get_serializer_context(self):
        context = super(CarView, self).get_serializer_context()
        context.update({"request": self.request})
        # EngineView.get_serializer_context(self)
        return context
    
class EngineView(generics.ListAPIView):
        queryset= Engine.objects.all()
        serializer_class= CarmodelengineSerializer
    
        def get_serializer_context(self):
            context = super(EngineView, self).get_serializer_context()
            context.update({"request": self.request})
            return context

# class EngineView(generics.ListAPIView):
#     queryset= Engine.objects.all()
#     serializer_class= CarmodelengineSerializer
    
#     def get_serializer_context(self):
#         context = super(EngineView, self).get_serializer_context()
#         context.update({"request1": self.request})
#         return context

    # def get(self, request, format=None):
    #     ans = CarModel.objects.all()
    #     print(request.user)
    #     user1 = AnonymousUser()
    #     if request.user==user1:
    #         serializer = CarSerializerAnonymous(ans,many=True)
    #     else:
    #         serializer = CarSerializerAutheticated(ans,many=True)
        
    #     return Response(serializer.data)



       