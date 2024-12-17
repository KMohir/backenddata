from rest_framework.routers import DefaultRouter

import api.views.youtube as views

router = DefaultRouter()
router.register("list", views.NewsListAPIView)
router.register("detail", views.NewsDetailAPIView)
router.register("header/list", views.HeaderNewsListAPIView)


urlpatterns = [] + router.urls
