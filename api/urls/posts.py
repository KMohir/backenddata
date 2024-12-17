from rest_framework.routers import DefaultRouter

import api.views.posts as views

router = DefaultRouter()
router.register(r"list/category/<int:pk>", views.PostListViewSet)
router.register("detail", views.PostDetailViewSet)

urlpatterns = [] + router.urls
