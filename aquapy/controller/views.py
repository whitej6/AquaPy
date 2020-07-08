from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import I2CMonitorAction
from .serializers import I2CMonitorActionSerializer


class I2CMonitorActionViewset(viewsets.ModelViewSet):
    """
    """
    permission_classes = (IsAuthenticated,)
    queryset = I2CMonitorAction.objects.all()
    serializer_class = I2CMonitorActionSerializer
