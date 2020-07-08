from pywemo import discover_devices
from rest_framework import viewsets, mixins
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import WemoSwitch
from .serializers import WemoSwitchSerializer


class WemoSwitchViewset(viewsets.ModelViewSet):
    """
    """
    permission_classes = (IsAuthenticated,)
    queryset = WemoSwitch.objects.all()
    serializer_class = WemoSwitchSerializer

    def discover(self, *args, **kwargs):
        """
        """
        devices = discover_devices()
        for device in devices:
            try:
                dev = WemoSwitch.objects.get(mac_address=device.mac)
                dev.name = device.name
                dev.device_type = device.device_type
                dev.save()
            except WemoSwitch.DoesNotExist:
                WemoSwitch.objects.create(
                    name=device.name,
                    mac_address=device.mac,
                    device_type=device.device_type
                )
        return Response({'devices_discovered': [i.name for i in devices]})
