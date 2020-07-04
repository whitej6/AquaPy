from django.contrib import admin

from .models import InfluxDB, I2CSensor, I2CJob


admin.site.register(InfluxDB)
admin.site.register(I2CSensor)
admin.site.register(I2CJob)
