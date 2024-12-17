from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import ListAPIView, RetrieveAPIView

import basic_app.models as models
from api.serializers.news import *


class NewsListAPIView(ListAPIView, GenericViewSet):
    """Barcha yangiliklar"""
    queryset = models.News.objects.select_related('created_by', "updated_by").order_by("-id")
    serializer_class = NewsListSerializer


class NewsDetailAPIView(RetrieveAPIView, GenericViewSet):
    """ News detail """
    queryset = models.News.objects.select_related('created_by', "updated_by").order_by("-id")
    serializer_class = NewsDetailSerializer
    lookup_field = 'slug'


class HeaderNewsListAPIView(ListAPIView, GenericViewSet):
    """Eng oxirgi 5 ta yangilik"""
    queryset = models.News.objects.select_related('created_by', "updated_by").order_by("-id")[:5]
    serializer_class = NewsListSerializer


class TheMostReadNewsListAPIView(ListAPIView, GenericViewSet):
    """Eng ko'p o'qilgan yangiliklar"""
    queryset = models.News.objects.select_related('created_by', "updated_by").order_by("-post_viewed_count")[:8]
    serializer_class = NewsListSerializer
