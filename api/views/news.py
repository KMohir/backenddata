from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import ListAPIView, RetrieveAPIView

from django.db.models import Q
from django.utils import timezone
import basic_app.models as models
from api.serializers.news import *

from api.serializers.news import NewsListSerializer,NewsDetailSerializer




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


class NewsSearchListAPIView(ListAPIView, GenericViewSet):
    queryset = models.News.objects.select_related('created_by', "updated_by").order_by("-id")
    serializer_class = NewsListSerializer

    def get_queryset(self):
        qs = models.News.objects
        search = self.request.query_params.get("search")
        if search:
            return qs.filter(
                Q(title__icontains=search)
            ).select_related('created_by', 'updated_by').order_by('-id')


class NewsDateFilterListAPIView(ListAPIView, GenericViewSet):
    queryset = models.News.objects.select_related('created_by', "updated_by").order_by("-id")
    serializer_class = NewsListSerializer

    def get_queryset(self):
        qs = models.News.objects
        date_str = self.request.query_params.get('date')
        if date_str:
            try:
                filter_date = timezone.datetime.strptime(date_str, "%Y-%m-%d").date()
                return qs.filter(
                    Q(created_at__date=filter_date)
                ).select_related('created_by', 'updated_by').order_by('-id')
            except ValueError:
                return qs.filter(
                    Q(created_at__date=timezone.now().date())
                ).select_related('created_by', 'updated_by').order_by('-id')
        else:
            return qs.filter(
                Q(created_at__date=timezone.now().date())
            ).select_related('created_by', 'updated_by').order_by('-id')
