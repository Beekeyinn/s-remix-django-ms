from django.conf import settings
from django.contrib.auth.models import AnonymousUser
from rest_framework.authentication import BaseAuthentication

from apps.remix.models import Session


def get_authentication_header(request):
    return request.META.get("HTTP_AUTHORIZATION")


class ShopifyBaseAuthentication(BaseAuthentication):
    def authenticate(self, request):
        if getattr(settings, "DEBUG") and "swagger" in request.META.get(
            "HTTP_REFERER", request.path
        ):
            try:
                user = Session.objects.get(
                    id=f'offline_{getattr(settings, "SHOPIFY_DEVELOPMENT_DOMAIN")}'
                )
                return (user, None)
            except Session.DoesNotExist:
                return (AnonymousUser(), None)
        else:
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
