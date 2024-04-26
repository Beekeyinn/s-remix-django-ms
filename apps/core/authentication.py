from django.contrib.auth.models import AnonymousUser
from rest_framework.authentication import BaseAuthentication

from apps.remix.models import Session


def get_authentication_header(request):
    return request.META.get("HTTP_AUTHORIZATION")


class ShopifyBaseAuthentication(BaseAuthentication):
    def authenticate(self, request):
        authentication = get_authentication_header(request)
        if authentication:
            try:
                user = Session.objects.get(accessToken=authentication)
            except Session.DoesNotExist:
                return (AnonymousUser(), None)
            else:
                return (user, None)
        else:
            return (AnonymousUser(), None)
