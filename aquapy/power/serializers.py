from rest_framework.serializers import ModelSerializer, ChoiceField

from .models import WemoSwitch


class WemoSwitchSerializer(ModelSerializer):
    """
    """
    class Meta:
        model = WemoSwitch
        fields = ['id', 'name', 'mac_address', 'device_type', 'desired_state']
        read_only_fields = ['id']
