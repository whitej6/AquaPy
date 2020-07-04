from django.db import models


class InfluxDB(models.Model):
    """

    """
    base_url = models.URLField(max_length=255)
    database = models.CharField(max_length=255)
    measurement = models.CharField(max_length=255)

    def __str__(self):
        return self.base_url

    def url(self):
        return f'{self.base_url}write?db={self.database}'
    
    def payload(self, sensor, value):
        return f'{self.measurement},sensor={sensor} value={value}'


class I2CSensor(models.Model):
    """

    """
    address = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class I2CJob(models.Model):
    """

    """
    sensor = models.ForeignKey(I2CSensor, on_delete=models.CASCADE)
    influxdb = models.ForeignKey(InfluxDB, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
