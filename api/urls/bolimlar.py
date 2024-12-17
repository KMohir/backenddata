

from rest_framework.routers import DefaultRouter

import api.views.bolimlar as views

router = DefaultRouter()
router.register("list", views.NewsListAPIView)



urlpatterns = [] + router.urls
