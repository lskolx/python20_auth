from django.shortcuts import render
from rest_framework import viewsets
from applications.order.models import Order
from .serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_serializer_context(self):
        return {'requests': self.request}

