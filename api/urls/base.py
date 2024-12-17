from django.urls import path, include

urlpatterns = [
    path("news/", include("api.urls.news")),
    path("posts/", include("api.urls.posts")),
    path("navbar/", include("api.urls.navbar")),
    path("interactive-map/", include("api.urls.interactive_map")),
    path("youtube/", include("api.urls.youtube")),
    path("elon/", include("api.urls.elon")),
    path("workers/", include("api.urls.workers")),
    path("banner/", include("api.urls.banner")),
    path("tuzilma/", include("api.urls.tuzilma")),
    path("maqsad/", include("api.urls.maqsad")),
    path("bolimlar/", include("api.urls.bolimlar")),

]
