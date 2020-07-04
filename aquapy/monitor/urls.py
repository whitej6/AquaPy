from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('sensor', views.I2CSensorsViewset)
router.register('job', views.I2CJobViewset)
router.register('influxdb', views.InfluxDBViewset)

app_name = 'monitor'
urlpatterns = [
    path('', include(router.urls))
]