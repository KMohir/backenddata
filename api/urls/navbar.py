from rest_framework.routers import DefaultRouter

import api.views.navbar as views

router = DefaultRouter()
router.register("list", views.NavbarListView)

urlpatterns = [] + router.urls
