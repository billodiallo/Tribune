from rest_framework import serializers
from .models import MoringaMerch
from rest_framework.views import APIView

class MoringaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoringaMerch
        fields = ('name','description','price')



class MerchSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoringaMerch
        fields = ('id','name', 'description', 'price')   


