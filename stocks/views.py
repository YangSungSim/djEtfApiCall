from django.shortcuts import render
from rest_framework import viewsets
from .serializer import StockSerializer
from .models import stock

# Create your views here.
class StockViewSet(viewsets.ModelViewSet):
    queryset = stock.objects.all();
    serializer_class = StockSerializer