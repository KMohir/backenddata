from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import ListAPIView, RetrieveAPIView

import basic_app.models.youtube as models
from api.serializers.youtube import *


class NewsListAPIView(ListAPIView, GenericViewSet):
    """Barcha yangiliklar"""
    queryset = models.Youtube.objects.select_related('created_by', "updated_by").order_by("-id")
    serializer_class = YoutubeListSerializer

class NewsDetailAPIView(RetrieveAPIView, GenericViewSet):
    """ News detail """
    queryset = models.Youtube.objects.select_related('created_by', "updated_by").order_by("-id")
    serializer_class = YoutubeListSerializer
    lookup_field = 'slug'


class HeaderNewsListAPIView(ListAPIView, GenericViewSet):
    """Eng oxirgi 5 ta yangilik"""
    queryset = models.Youtube.objects.select_related('created_by', "updated_by").order_by("-id")[:5]
    serializer_class = YoutubeListSerializer




