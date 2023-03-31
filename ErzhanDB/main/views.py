from django.shortcuts import render
from rest_framework import viewsets
from .models import PodBrand, SnusBrand, SingleBrand, ConsumablesBrand, LiquidBrand
from .serializers import PodBrandSerializer, SnusBrandSerializer, SingleBrandSerializer, ConsumablesBrandSerializer, \
    LiquidBrandSerializer
from .serializers import (PodSerializer, SnusSerializer, SingleSerializer,
                          ConsumablesSerializer, LiquidSerializer)
from .models import Pod, Snus, Single, Consumable, Liquid


class PodBrandViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = PodBrand.objects.all()
    serializer_class = PodBrandSerializer


class SnusBrandViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SnusBrand.objects.all()
    serializer_class = SnusBrandSerializer


class SingleBrandViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SingleBrand.objects.all()
    serializer_class = SingleBrandSerializer


class ConsumablesBrandViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ConsumablesBrand.objects.all()
    serializer_class = ConsumablesBrandSerializer


class LiquidBrandViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = LiquidBrand.objects.all()
    serializer_class = LiquidBrandSerializer


class PodViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Pod.objects.all()
    serializer_class = PodSerializer


class SnusViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Snus.objects.all()
    serializer_class = SnusSerializer


class SingleViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Single.objects.all()
    serializer_class = SingleSerializer


class ConsumablesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Consumable.objects.all()
    serializer_class = ConsumablesSerializer


class LiquidViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Liquid.objects.all()
    serializer_class = LiquidSerializer
