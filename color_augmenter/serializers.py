from rest_framework import serializers
from color_augmenter.models import IllustrationSet


class IllustrationSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = IllustrationSet
        fields = (
            "id",
            "name",
            "outNum",
            "illustrationList",
            "created",
            "updated",
        )
