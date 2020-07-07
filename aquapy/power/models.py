from django.db import models


class WemoSwitch(models.Model):
    """

    """
    DESIRED_STATE_CHOICES = [
        'On',
        'Off',
        'Scheduled'
    ]

    name = models.CharField(max_length=255)
    mac_address = models.CharField(max_length=255, unique=True)
    device_type = models.CharField(max_length=255)
    desired_state = models.CharField(max_length=255, choices=DESIRED_STATE_CHOICES)

    def __str__(self):
        return self.name
