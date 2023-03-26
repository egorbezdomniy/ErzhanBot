from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('liquids', views.getLiquids),
    path('liquids/<str:pk>', views.getLiquid),
]
