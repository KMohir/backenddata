from rest_framework.routers import DefaultRouter

import api.views.interactive_map as views

router = DefaultRouter()
router.register("list", views.InteractiveMapListViewSet)

urlpatterns = router.urls
