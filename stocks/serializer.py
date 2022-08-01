from rest_framework import serializers
from .models import stock

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = stock
        fields = ('date','open','high','low','close','adj_close','volume')