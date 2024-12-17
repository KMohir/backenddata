from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.viewsets import GenericViewSet

import basic_app.models as models
from api.serializers.posts import *


class PostListViewSet(GenericViewSet, ListAPIView):
    queryset = models.Posts.objects.select_related('created_by', 'updated_by', 'navbar')
    serializer_class = PostsListSerializer

    def list(self, request, pk=None):
        queryset = self.get_queryset().filter(category_id=pk) if pk else self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class PostDetailViewSet(GenericViewSet, RetrieveAPIView):
    queryset = models.Posts.objects.select_related('created_by', 'updated_by', 'navbar')
    serializer_class = PostsDetailSerializer
    lookup_field = 'slug'
