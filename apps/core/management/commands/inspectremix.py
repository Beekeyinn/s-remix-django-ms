from typing import Any

from django.core.management.commands.inspectdb import Command as InspectDBCommand


class Command(InspectDBCommand):
    def handle(self, *args: Any, **options: Any) -> str | None:
        options["database"] = "remix"
        return super().handle(*args, **options)
