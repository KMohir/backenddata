from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import ListAPIView, RetrieveAPIView

import basic_app.models.bolimlar as models
from api.serializers.bolimlar import *


class NewsListAPIView(ListAPIView, GenericViewSet):
    """Barcha yangiliklar"""
    queryset = models.bolimlar.objects.order_by("-id")
    serializer_class = AdministratorListSerializer