from django.shortcuts import render
from django.http import JsonResponse

def getRoutes(request):
    routes = [
        'GET /api',
        'GET /api/liquids',
        'GET /api/liquids/:id'
    ]
    return JsonResponse(routes, safe=False)