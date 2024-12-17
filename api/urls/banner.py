from rest_framework.routers import DefaultRouter

import api.views.banner as views

router = DefaultRouter()
router.register("list", views.NewsListAPIView)
router.register("detail", views.NewsDetailAPIView)
router.register("header/list", views.HeaderNewsListAPIView)
router.register("most_read/list", views.TheMostReadNewsListAPIView)

urlpatterns = [] + router.urls
