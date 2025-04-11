from django.db import models
from datetime import datetime


class Transactions(models.Model):
    from_ac = models.CharField(max_length=50)
    from_ac_name = models.CharField(max_length=60)
    from_ac_routing_no = models.CharField(max_length=20)
    to_ac = models.CharField(max_length=50)
    to_ac_name = models.CharField(max_length=60)
    to_ac_routing_no = models.CharField(max_length=20)
    amount = models.FloatField()
    service_charge = models.FloatField()
    transaction_status = models.CharField(max_length=30)
    created_datetime = models.DateTimeField(default=datetime.now)
    updated_datetime = models.DateTimeField(default=datetime.now)

