from rest_framework.exceptions import APIException


class CustomException(APIException):
    status_code = 422
    default_detail = "Something went wrong."
