from datetime import datetime
from rest_framework import serializers


class TransactionSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    from_ac = serializers.CharField(max_length=50)
    from_ac_name = serializers.CharField(max_length=60)
    from_ac_routing_no = serializers.CharField()
    to_ac = serializers.CharField(max_length=50)
    to_ac_name = serializers.CharField(max_length=60)
    to_ac_routing_no = serializers.CharField()
    amount = serializers.FloatField()
    service_charge = serializers.FloatField()
    transaction_status = serializers.CharField(max_length=30)
    created_datetime = serializers.DateTimeField(default=datetime.now)
    updated_datetime = serializers.DateTimeField(default=datetime.now)
