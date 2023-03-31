from django.urls import path, include
from rest_framework import routers
from .views import (PodBrandViewSet, SnusBrandViewSet, SingleBrandViewSet, 
                    ConsumablesBrandViewSet, LiquidBrandViewSet,
                    PodViewSet, SnusViewSet, SingleViewSet, 
                    ConsumablesViewSet, LiquidViewSet)

router = routers.DefaultRouter()
router.register(r'pod-brands', PodBrandViewSet)
router.register(r'snus-brands', SnusBrandViewSet)
router.register(r'single-brands', SingleBrandViewSet)
router.register(r'consumables-brands', ConsumablesBrandViewSet)
router.register(r'liquid-brands', LiquidBrandViewSet)

router.register(r'pods', PodViewSet)
router.register(r'snuses', SnusViewSet)
router.register(r'singles', SingleViewSet)
router.register(r'consumables', ConsumablesViewSet)
router.register(r'liquids', LiquidViewSet)

urlpatterns = [
    path('', include(router.urls)),
]