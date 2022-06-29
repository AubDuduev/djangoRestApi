"""restApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers

from women.views import *

router = routers.SimpleRouter()
router.register(r'women', WomenViewSet)
womenPath = 'women'
womenDeletePath = 'women-delete'
apiPath = 'api'
v1Path = 'v1'
womenDeletePath = 'women-delete'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/women', WomenAPIView.as_view()),
    path('api/v1/womenlists/', WomenAPIListView.as_view()),
    path('api/v1/womenlist/<int:pk>/', WomenAPIView.as_view()),
    path('api/v1/womenlistupdate/<int:pk>/', WomenAPIUpdateView.as_view()),
    path('api/v1/womenget/', WomenViewSet.as_view({'get': 'list'})),
    path('api/v1/women/<int:pk>/', WomenViewSet.as_view({'put': 'update'})),
    path('api/v1/women-delete/<int:pk>/', WomenAPIDestroyView.as_view()),
    path('api/v1/women-update/<int:pk>/', WomenAPIUpdateView.as_view()),
    path('api/v1/women-list/', WomenAPIListView.as_view()),
    path('api/v1/auth/', include('rest_framework.urls')),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]