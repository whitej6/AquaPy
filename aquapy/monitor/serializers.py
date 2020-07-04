from rest_framework.serializers import ModelSerializer, ChoiceField

from .models import I2CSensor, I2CJob, InfluxDB


class InfluxDBSerializer(ModelSerializer):
    """
    """
    class Meta:
        model = InfluxDB
        fields = ['id', 'base_url', 'database', 'measurement', 'url']
        read_only_fields = ['id', 'url']


class I2CSensorSerializer(ModelSerializer):
    """
    """
    class Meta:
        model = I2CSensor
        fields = ['id', 'address', 'name', 'slug']
        read_only_fields = ['id', 'address', 'slug']


class I2CJobSerializer(ModelSerializer):
    """
    """
    influxdb = InfluxDBSerializer
    class Meta:
        model = I2CJob
        fields = ['id', 'sensor', 'name', 'influxdb']
        read_only_fields = ['id']
