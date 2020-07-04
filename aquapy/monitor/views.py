from rest_framework import viewsets, mixins
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import I2CSensor, InfluxDB, I2CJob
from .serializers import I2CSensorSerializer, I2CJobSerializer, InfluxDBSerializer


class I2CSensorsViewset(viewsets.GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin):
    """
    """
    permission_classes = (IsAuthenticated,)
    queryset = I2CSensor.objects.all()
    serializer_class = I2CSensorSerializer


class InfluxDBViewset(viewsets.ModelViewSet):
    """
    """
    permission_classes = (IsAuthenticated,)
    queryset = InfluxDB.objects.all()
    serializer_class = InfluxDBSerializer


class I2CJobViewset(viewsets.ModelViewSet):
    """
    """
    permission_classes = (IsAuthenticated,)
    queryset = I2CJob.objects.all()
    serializer_class = I2CJobSerializer

