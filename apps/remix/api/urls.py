from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.remix.api.views import (
    ProfileModelViewSet,
    SessionModelViewSet,
    SettingModelViewSet,
)

router = DefaultRouter()
router.register("settings", SettingModelViewSet, basename="settings")
router.register("sessions", SessionModelViewSet, basename="sessions")
router.register("profiles", ProfileModelViewSet, basename="profiles")

urlpatterns = [
    path("", include(router.urls)),
]
