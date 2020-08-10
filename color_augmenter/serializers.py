from rest_framework import serializers
from color_augmenter.models import IllustrationSet, Image

# import sys
# import subprocess

from drfx.settings import BASE_DIR, MEDIA_ROOT
from utils.WBAugmenter_Python.wbAug import parse_args, augment_images


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ("image",)


class IllustrationSetSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True, read_only=True)

    class Meta:
        model = IllustrationSet
        fields = (
            "id",
            "name",
            "outNum",
            "illustrationList",
            "images",
            "created",
            "updated",
        )

        extra_kwargs = {"images": {"read_only": True}}

    def create(self, validated_data):
        imgpath = MEDIA_ROOT + "/uploads/" + str(validated_data["illustrationList"])
        output_image_number = validated_data["outNum"]

        illustration_set = IllustrationSet.objects.create(**validated_data)
        processed_images_paths = augment_images(
            input_image_filename=imgpath, out_number=output_image_number
        )

        for i in processed_images_paths:
            Image.objects.create(image=i, illustration_set=illustration_set)

        return illustration_set
