from .models import CarModel,Engine,Price
from rest_framework_serializer_field_permissions import fields                                     
from rest_framework_serializer_field_permissions.serializers import FieldPermissionSerializerMixin  
from rest_framework_serializer_field_permissions.permissions import IsAuthenticated    
from rest_framework import serializers

class CarmodelengineSerializer(FieldPermissionSerializerMixin, serializers.ModelSerializer):

    maker = fields.CharField(permission_classes=(IsAuthenticated(), ))    
    class Meta:
            model =  Engine
            fields = ['id','displacement','power','maker']

class CarmodelPriceSerializer(FieldPermissionSerializerMixin, serializers.ModelSerializer):

    price = fields.IntegerField(permission_classes=(IsAuthenticated(), ))    
    id    = fields.IntegerField(permission_classes=(IsAuthenticated(), ))    

    class Meta:
            model  =  Price
            fields =  ['id','price']

class CarSerializerAutheticated(FieldPermissionSerializerMixin, serializers.ModelSerializer):
    
    engine = CarmodelengineSerializer(read_only=True)
    price = CarmodelPriceSerializer(read_only=True)

    class Meta:
        model = CarModel
        fields = ['id','car_name','engine','price']
        depth = 2

    