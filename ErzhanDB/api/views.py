from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Liquid
from .serializers import LiquidSerializer


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/liquids',
        'GET /api/liquids/:id'
    ]
    return Response(routes)


@api_view(['GET'])
def getLiquids(request):
    liquids = Liquid.objects.all()
    serializer = LiquidSerializer(liquids, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getLiquid(request, pk):
    liquid = Liquid.objects.get(id=pk)
    serializer = LiquidSerializer(liquid, many=False)
    return Response(serializer.data)

