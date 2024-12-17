from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from api.drf_yasg import yasg_schema_view
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path("api/", include("api.urls.base")),
                  path('api-auth/', include('rest_framework.urls')),
                  path('documents/', yasg_schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
                  path('swagger/', yasg_schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
              ] + i18n_patterns(

    path("api/", include("api.urls.base")),
    path('i18/', include('django.conf.urls.i18n')),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

