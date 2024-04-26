from rest_framework.viewsets import ModelViewSet

from apps.remix.api.Settings.serializers import SettingModelSerializer
from apps.remix.models import Settings


class SettingModelViewSet(ModelViewSet):
    serializer_class = SettingModelSerializer
    queryset = Settings.objects.all()
    http_method_names = ["get"]
