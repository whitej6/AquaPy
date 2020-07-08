from rest_framework.serializers import ModelSerializer

from .models import I2CMonitorAction


class I2CMonitorActionSerializer(ModelSerializer):
    """
    """

    class Meta:
        model = I2CMonitorAction
        fields = [
            'id',
            'name',
            'description',
            'failed_state',
            'failed_threshold',
            'recovered_state',
            'recovered_threshold',
            'job',
            'high_low_threshold',
            'power_switch'
        ]
        read_only_fields = ['id']
