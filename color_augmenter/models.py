from django.db import models


# List of illustrations generated after the colour augmenter run
class IllustrationSet(models.Model):
    name = models.CharField(max_length=255)
    outNum = models.IntegerField()
    illustrationList = models.ImageField(
        upload_to="uploads/", blank=True, null=True, max_length=256
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Image(models.Model):
    image = models.ImageField(
        upload_to="uploads/", blank=True, null=True, max_length=256
    )
    illustration_set = models.ForeignKey(
        IllustrationSet, default=None, related_name="images", on_delete=models.PROTECT
    )
