from rest_framework.viewsets import ModelViewSet

from apps.remix.api.Profile.serializers import ProfileModelSerializer
from apps.remix.models import Profile


class ProfileModelViewSet(ModelViewSet):
    serializer_class = ProfileModelSerializer
    queryset = Profile.objects.all()
    http_method_names = ["get"]
