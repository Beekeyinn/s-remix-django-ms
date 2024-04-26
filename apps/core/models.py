from django.db import models


# Create your models here.
class SingleTonModel(models.Model):
    @classmethod
    def object(cls):
        return cls._default_manager.all().first()

    def save(self, *args, **kwargs):
        queryset = self.__class__.objects.filter().first()
        if queryset is None:
            self.pk = 1
        else:
            self.pk = queryset.id
        return super().save(*args, **kwargs)

    class Meta:
        abstract = True
