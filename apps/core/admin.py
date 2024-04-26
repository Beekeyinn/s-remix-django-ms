from collections.abc import Sequence
from copy import copy

from django.contrib import admin
from django.db.models import TextField
from django.http import HttpRequest


# Register your models here.
class RemixModelAdmin(admin.ModelAdmin):

    using = "remix"

    def save_model(self, request, obj, form, change):

        obj.save(using=self.using)

    def delete_model(self, request, obj):

        obj.delete(using=self.using)

    def get_queryset(self, request):

        return super().get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):

        return super().formfield_for_foreignkey(
            db_field, request, using=self.using, **kwargs
        )

    def formfield_for_manytomany(self, db_field, request, **kwargs):

        return super().formfield_for_manytomany(
            db_field, request, using=self.using, **kwargs
        )

    def get_list_display(self, request: HttpRequest) -> Sequence[str]:

        fields = self.model._meta.get_fields()
        fields_copy = copy(fields)
        field_names = [
            field.name
            for field in fields_copy
            if not isinstance(field, TextField) and not hasattr(field, "field")
        ]
        return field_names


class RemixTabularInline(admin.TabularInline):
    using = "remix"

    def get_queryset(self, request):
        return super().get_queryset(request).using(self.using)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        return super().formfield_for_foreignkey(
            db_field, request, using=self.using, **kwargs
        )

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        return super().formfield_for_manytomany(
            db_field, request, using=self.using, **kwargs
        )
