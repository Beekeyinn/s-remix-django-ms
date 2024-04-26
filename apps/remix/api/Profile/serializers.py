from rest_framework import serializers
from apps.remix.models import Profile


class ProfileModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"
