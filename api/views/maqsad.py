from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import ListAPIView, RetrieveAPIView

import basic_app.models.maqsad as models
from api.serializers.maqsad import *


class NewsListAPIView(ListAPIView, GenericViewSet):
    """Barcha yangiliklar"""
    queryset = models.maqsad.objects.order_by("-id")
    serializer_class = AdministratorListSerializer