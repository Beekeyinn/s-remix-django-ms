from rest_framework import serializers

from apps.remix.models import Session


class SessionModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = "__all__"
