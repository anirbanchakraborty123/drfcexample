from django.contrib.auth import get_user_model
from rest_framework import serializers, validators
from .models import CarModel,Engine,Price
from django.contrib.auth.models import AnonymousUser
from rest_framework_serializer_field_permissions import fields                                      # <--
from rest_framework_serializer_field_permissions.serializers import FieldPermissionSerializerMixin  # <--
from rest_framework_serializer_field_permissions.permissions import IsAuthenticated    

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = '__all__'
        depth = 2
    

class UnAuthorizedEngineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Engine
        exclude = ['maker',]


class UnAuthorizedCarSerializer(serializers.ModelSerializer):

    engine = UnAuthorizedEngineSerializer()
    
    class Meta:
        model = CarModel
        fields = ['id', 'car_name', 'engine']
