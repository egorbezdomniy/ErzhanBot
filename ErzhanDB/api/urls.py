from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),

    path('liquids', views.getLiquids),
    path('liquids/<str:pk>', views.getLiquid),

    path('pods', views.getPods),
    path('pods/<str:pk>', views.getPod),
        
    path('snus', views.getSnusAll),
    path('snus/<str:pk>', views.getSnus),

    path('single_uses', views.getSingleUses),
    path('single_uses/<str:pk>', views.getSingleUse),

    path('consumables', views.getConsumables),
    path('consumables/<str:pk>', views.getConsumable),

]
