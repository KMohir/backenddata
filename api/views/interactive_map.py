from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import ListAPIView, RetrieveAPIView

import basic_app.models as models
from api import InteractiveMapSerializer
from api.serializers.interactive_map import *


class InteractiveMapListViewSet(ListAPIView, GenericViewSet):
    queryset = models.InteractiveMap.objects.all()
    serializer_class = InteractiveMapSerializer
