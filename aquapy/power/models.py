from django.db import models


class WemoSwitch(models.Model):
    """

    """
    name = models.CharField(max_length=255)
    mac_address = models.CharField(max_length=255, unique=True)
    device_type = models.CharField(max_length=255)

    def __str__(self):
        return self.name
