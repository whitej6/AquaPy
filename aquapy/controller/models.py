from django.db import models

from monitor.models import I2CJob
from power.models import WemoSwitch


class I2CMonitorAction(models.Model):
    """

    """
    STATE_CHOICES = [
        ('on', 'On'),
        ('off', 'Off'),
        ('scheduled', 'Scheduled')
    ]
    HIGH_LOW_THRESHOLD_CHOICES = [
        ('high', 'High'),
        ('low', 'Low')
    ]

    name = models.CharField(max_length=255, unique=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    failed_state = models.CharField(
        max_length=255,
        choices=STATE_CHOICES,
        default='off'
    )
    failed_threshold = models.FloatField()
    recovered_state = models.CharField(
        max_length=255,
        choices=STATE_CHOICES,
        default='on'
    )
    recovered_threshold = models.FloatField()
    job = models.ForeignKey(I2CJob, on_delete=models.CASCADE)
    high_low_threshold = models.CharField(max_length=255, choices=HIGH_LOW_THRESHOLD_CHOICES)
    power_switch = models.ForeignKey(WemoSwitch, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
