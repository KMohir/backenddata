from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import ListAPIView, RetrieveAPIView

import basic_app.models as models
from api.serializers.banner import *


class NewsListAPIView(ListAPIView, GenericViewSet):
    """Barcha yangiliklar"""
    queryset = models.Banner.objects.select_related('created_by', "updated_by").order_by("-id")
    serializer_class = BannerListSerializer


class NewsDetailAPIView(RetrieveAPIView, GenericViewSet):
    """ News detail """
    queryset = models.Banner.objects.select_related('created_by', "updated_by").order_by("-id")
    serializer_class = BannerDetailSerializer
    lookup_field = 'slug'


class HeaderNewsListAPIView(ListAPIView, GenericViewSet):
    """Eng oxirgi 5 ta yangilik"""
    queryset = models.Banner.objects.select_related('created_by', "updated_by").order_by("-id")[:5]
    serializer_class = BannerListSerializer


class TheMostReadNewsListAPIView(ListAPIView, GenericViewSet):
    """Eng ko'p o'qilgan yangiliklar"""
    queryset = models.Banner.objects.select_related('created_by', "updated_by").order_by("-post_viewed_count")[:8]
    serializer_class = BannerListSerializer
