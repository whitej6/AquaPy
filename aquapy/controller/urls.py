from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('action', views.I2CMonitorActionViewset)

app_name = 'controller'
urlpatterns = [
    path('', include(router.urls))
]