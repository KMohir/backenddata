from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import ListAPIView, RetrieveAPIView

import basic_app.models.workers as models
from api.serializers.workers import *


class NewsListAPIView(ListAPIView, GenericViewSet):
    """Barcha yangiliklar"""
    queryset = models.Administrator.objects.order_by("-id")
    serializer_class = AdministratorListSerializer