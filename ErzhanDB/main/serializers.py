from rest_framework import serializers
from .models import PodBrand, SnusBrand, SingleBrand, ConsumablesBrand, LiquidBrand, Pod, Snus, Single, Consumable, \
    Liquid


class PodBrandSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)

    class Meta:
        model = PodBrand
        fields = ('id', 'name', 'image')


class SnusBrandSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)

    class Meta:
        model = SnusBrand
        fields = ('id', 'name', 'image')


class SingleBrandSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)

    class Meta:
        model = SingleBrand
        fields = ('id', 'name', 'image')


class ConsumablesBrandSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)

    class Meta:
        model = ConsumablesBrand
        fields = ('id', 'name', 'image')


class LiquidBrandSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)

    class Meta:
        model = LiquidBrand
        fields = ['id', 'name', 'image']


class PodSerializer(serializers.ModelSerializer):
    brand = PodBrandSerializer()

    class Meta:
        model = Pod
        fields = ('id', 'name', 'price', 'amount', 'brand')


class SnusSerializer(serializers.ModelSerializer):
    brand = SnusBrandSerializer()

    class Meta:
        model = Snus
        fields = ('id', 'name', 'price', 'amount', 'brand')


class SingleSerializer(serializers.ModelSerializer):
    brand = SingleBrandSerializer()

    class Meta:
        model = Single
        fields = ('id', 'name', 'price', 'amount', 'brand')


class ConsumablesSerializer(serializers.ModelSerializer):
    brand = ConsumablesBrandSerializer()

    class Meta:
        model = Consumable
        fields = ('id', 'name', 'price', 'amount', 'brand')


class LiquidSerializer(serializers.ModelSerializer):
    brand = LiquidBrandSerializer()

    class Meta:
        model = Liquid
        fields = ('id', 'name', 'price', 'amount', 'brand')
