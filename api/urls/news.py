from rest_framework.routers import DefaultRouter

import api.views.news as views

router = DefaultRouter()
router.register("list", views.NewsListAPIView)
router.register("detail", views.NewsDetailAPIView)
router.register("search", views.NewsSearchListAPIView)
router.register("header/list", views.HeaderNewsListAPIView)
router.register("date-filter", views.NewsDateFilterListAPIView)
router.register("most_read/list", views.TheMostReadNewsListAPIView)

urlpatterns = [] + router.urls
