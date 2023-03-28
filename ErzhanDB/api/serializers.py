from .models import Liquid, Pod, Snus, SingleUse, Consumable
from rest_framework.serializers import ModelSerializer, SlugRelatedField


class LiquidSerializer(ModelSerializer):
    class Meta:
        model = Liquid
        fields = '__all__'


class PodSerializer(ModelSerializer):
    class Meta:
        model = Pod
        fields = '__all__'


class SnusSerializer(ModelSerializer):
    class Meta:
        model = Snus
        fields = '__all__'


class SingleUseSerializer(ModelSerializer):
    class Meta:
        model = SingleUse
        fields = '__all__'


class ConsumableSerializer(ModelSerializer):
    class Meta:
        model = Consumable
        fields = '__all__'
