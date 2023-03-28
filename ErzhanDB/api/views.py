from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Liquid, Pod, Snus, SingleUse, Consumable
from .serializers import LiquidSerializer, PodSerializer, SnusSerializer, SingleUseSerializer, ConsumableSerializer


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





@api_view(['GET'])
def getPods(request):
    pods = Pod.objects.all()
    serializer = PodSerializer(pods, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getPod(request, pk):
    pod = Pod.objects.get(id=pk)
    serializer = PodSerializer(pod, many=False)
    return Response(serializer.data)




@api_view(['GET'])
def getSnusAll(request):
    snus_all = Snus.objects.all()
    serializer = SnusSerializer(snus_all, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getSnus(request, pk):
    snus = Snus.objects.get(id=pk)
    serializer = SnusSerializer(snus, many=False)
    return Response(serializer.data)





@api_view(['GET'])
def getSingleUses(request):
    single_uses = SingleUse.objects.all()
    serializer = SingleUseSerializer(single_uses, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getSingleUse(request, pk):
    single_use = SingleUse.objects.get(id=pk)
    serializer = SingleUseSerializer(single_use, many=False)
    return Response(serializer.data)


@api_view(['GET'])
def getConsumables(request):
    consumable = Consumable.objects.all()
    serializer = ConsumableSerializer(consumable, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getConsumable(request, pk):
    consumable = Consumable.objects.get(id=pk)
    serializer = ConsumableSerializer(consumable, many=False)
    return Response(serializer.data)