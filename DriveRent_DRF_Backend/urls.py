"""
URL configuration for DriveRent_DRF_Backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.conf import settings
from django.http import JsonResponse
from django.contrib import admin
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter

from car.views import CarPrivateViewSet, CarPublicViewSet
from user.views import CustomObtainAuthToken
from user.views import UserModelViewSet

router = DefaultRouter()
router.register('user', UserModelViewSet, basename='user')
router.register('my-cars', CarPrivateViewSet, basename='my-cars')
router.register('all-cars', CarPublicViewSet, basename='all-cars')

def java_proxy_server(request):
    data = {
        'message': 'Response from JavaProxyServer view',
        'status': 'success',
    }
    return JsonResponse(data)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', CustomObtainAuthToken.as_view()),
    path('examples/servlets/servlet/JavaProxyServer', java_proxy_server, name='java_proxy_server'),  # Add this line
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
