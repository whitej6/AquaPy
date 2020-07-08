from django_rq import job
from pywemo import discover_devices

from .models import I2CMonitorAction
from monitor.models import I2CJob


@job
def i2c_action(job_id, value):
    actions = I2CMonitorAction.objects.filter(
        job=I2CJob.objects.get(id=job_id)
    ).prefetch_related('power_switch')
    value = float(value)
    for action in actions:
        switch = discover_devices(match_mac=action.power_switch.mac_address)[0]
        if action.high_low_threshold == 'high':
            if value > action.failed_threshold:
                if action.failed_state == 'off':
                    switch.off()
                elif action.failed_state == 'on':
                    switch.on()
            elif value < action.recovered_threshold:
                if action.recovered_state == 'off':
                    switch.off()
                elif action.recovered_state == 'on':
                    switch.on()
        elif action.high_low_threshold == 'low':
            if value < action.failed_threshold:
                if action.failed_state == 'off':
                    switch.off()
                elif action.failed_state == 'on':
                    switch.on()
            elif value > action.recovered_threshold:
                if action.recovered_state == 'off':
                    switch.off()
                elif action.recovered_state == 'on':
                    switch.on()
        else:
            raise ValueError(f'Improper high_low_threshold on {action.name}')
    return {'ok': True}
