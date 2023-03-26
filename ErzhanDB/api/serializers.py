from .models import Liquid
from rest_framework.serializers import ModelSerializer

class LiquidSerializer(ModelSerializer):
    class Meta:
        model = Liquid
        fields = '__all__'
