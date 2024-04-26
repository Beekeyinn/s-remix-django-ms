from rest_framework.viewsets import ModelViewSet

from apps.remix.api.Session.serializers import SessionModelSerializer
from apps.remix.models import Session


class SessionModelViewSet(ModelViewSet):
    serializer_class = SessionModelSerializer
    queryset = Session.objects.all()
    http_method_names = ["get"]
