from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version="v1",
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
]

urlpatterns += [
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]

urlpatterns += [
    path("api/v1/", include("base.api_urls")),
]

if not settings.DEBUG and settings.DEV_TEST:
    urlpatterns += [
        re_path(
            r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}
        ),
    ]
# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
