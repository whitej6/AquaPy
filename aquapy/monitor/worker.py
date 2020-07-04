import os

from django_rq import job
import requests
from requests.auth import HTTPBasicAuth

from .atlas_i2c import AtlasI2C
from .models import I2CJob

@job
def query_sensors():
    jobs = I2CJob.objects.all().prefetch_related('sensor', 'influxdb')
    for job in jobs:
        sensor = AtlasI2C(address=job.sensor.address)
        value = sensor.query('r')['value']
        sensor.close()
        if job.sensor.slug == 'temp':
            value = (value * 9/5) + 32
        value = str(round(value, 2))
        r = requests.post(
            job.influxdb.url(),
            data=job.influxdb.payload(job.sensor.slug, value),
            auth=HTTPBasicAuth(
                os.environ['INFLUXDB_USER'],
                os.environ['INFLUXDB_USER_PASSWORD']
            )
        )
        if not r.ok:
            print(r.status_code)
            print(r.json())
            raise ValueError('Job Failed')
