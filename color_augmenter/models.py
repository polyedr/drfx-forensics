from django.db import models


# List of illustrations generated after the colour augmenter run
class IllustrationSet(models.Model):
    name = models.CharField(max_length=255)
    outNum = models.IntegerField()
    illustrationList = models.ImageField(upload_to="illustrations")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
