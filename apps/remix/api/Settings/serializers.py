from rest_framework import serializers

from apps.remix.models import Settings


class SettingModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = "__all__"
