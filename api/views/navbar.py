from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import ListAPIView, RetrieveAPIView

import basic_app.models as models
from api.serializers.navbar import *


class NavbarListView(ListAPIView, GenericViewSet):
    queryset = models.Navbar.objects.select_related("parent").filter(status=models.NavbarStatus.base, visible=True)
    serializer_class = NavbarListSerializer
