from typing import Any

from django.conf import settings
from django.core.management.commands.inspectdb import Command as InspectDBCommand
from django.db import connections


class Command(InspectDBCommand):
    def handle(self, *args: Any, **options: Any) -> str | None:
        options["database"] = "remix"
        self.create_django_schema(options)
        return super().handle(*args, **options)

    def create_django_schema(self, options: Any) -> None:
        connection = connections[options["database"]]
        with connection.cursor() as cursor:
            sql = f"CREATE SCHEMA IF NOT EXISTS {settings.SCHEMA};"
            cursor.execute(sql)
