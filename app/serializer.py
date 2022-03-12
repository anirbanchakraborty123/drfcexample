from .models import CarModel,Engine,Price
from rest_framework_serializer_field_permissions import fields                                     
from rest_framework_serializer_field_permissions.serializers import FieldPermissionSerializerMixin  
from rest_framework_serializer_field_permissions.permissions import IsAuthenticated    
from rest_framework import serializers
from collections import OrderedDict


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

    def to_representation(self, instance):
        result = super(CarmodelPriceSerializer, self).to_representation(instance)
        if bool(result)==False:
            return None 
        else:
            return OrderedDict([(key, result[key]) for key in result if result is not None ])


   
class CarSerializerAutheticated(FieldPermissionSerializerMixin, serializers.ModelSerializer):
    
    engine = CarmodelengineSerializer(read_only=True)
    price = CarmodelPriceSerializer(required=False)

    class Meta:
        model = CarModel
        fields = ['id','car_name','engine','price']
        depth = 2
    
    def to_representation(self, instance):
        result = super(CarSerializerAutheticated, self).to_representation(instance)
        return OrderedDict([(key, result[key]) for key in result if result[key] is not None ])


   