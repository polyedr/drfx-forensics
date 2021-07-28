# Create your models here.
from django.db import models
from jsonfield import JSONField


class SmartcropImage(models.Model):
    image = models.ImageField(
        upload_to="uploads/", blank=True, null=True, max_length=256
    )
    width = models.IntegerField()
    height = models.IntegerField()
    result = JSONField(blank=True, default=[])

    def __str__(self):
        return "{}".format(self.pk)
