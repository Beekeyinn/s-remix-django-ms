from django.urls import include, path

urlpatterns = [
    path("", include("apps.remix.api.urls")),
]
