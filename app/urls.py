import os
from django.http import JsonResponse, HttpResponse
from django.urls import path

def index(_request):
    return JsonResponse({'service': 'django', 'databaseConfigured': bool(os.getenv('DATABASE_URL'))})

def healthz(_request):
    return HttpResponse(status=204)

urlpatterns = [path('', index), path('healthz', healthz)]
