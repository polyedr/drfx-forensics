from rest_framework import serializers

import json
import sys

import smartcrop
from PIL import Image as ImagePIL

import smartcropsize
from drfx.settings import MEDIA_ROOT
from smartcropsize.models import SmartcropImage


class SmartcropImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmartcropImage
        fields = (
            "id",
            "image",
            "width",
            "height",
            "result",
        )

        extra_kwargs = {
            "result": {"read_only": True},
            "width": {"write_only": True},
            "height": {"write_only": True},
            "image": {"write_only": True},
        }

    def create(self, validated_data):
        imgpath = MEDIA_ROOT + "/uploads/" + str(validated_data["image"])
        width = validated_data["width"]
        height = validated_data["height"]

        smartcropimage = SmartcropImage.objects.create(**validated_data)

        image = ImagePIL.open(imgpath)
        sc = smartcrop.SmartCrop()
        result = sc.crop(image, width, height)

        smartcropimage.result = result

        return smartcropimage
