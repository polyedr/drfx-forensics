from rest_framework import serializers

from PIL import Image as ImagePIL

import os
import subprocess

from drfx.settings import BASE_DIR, MEDIA_ROOT, MEDIA_URL
from forensics.models import ForensicsData


class ForensicsDataSerializer(serializers.ModelSerializer):
    forensics_data_text = serializers.CharField(allow_blank=True)
    flag = serializers.CharField()
    image = serializers.ImageField(
        max_length=None, allow_empty_file=True, required=False, write_only=True
    )

    class Meta:
        model = ForensicsData
        fields = (
            "id",
            "forensics_data_text",
            "flag",
            "image",
            "created",
            "modified",
        )

        extra_kwargs = {"flag": {"write_only": True}, "forensics_data_text": {"read_only": True}}

    def create(self, validated_data):
        imgpath = MEDIA_ROOT + "/uploads/" + str(validated_data["image"])
        outputimgpath = (
                "/home/admin/Public/work/csh/ai_design_apis/drfx-forensics/drfx/utils/code/output/forensics4_"
                + str(validated_data["image"])
        )

        # Saving uploaded image
        img = ImagePIL.open(validated_data["image"])
        flag = [validated_data["flag"]]

        img.save(imgpath)

        file_path = [imgpath]

        wpath = (
            "/home/admin/Public/work/csh/ai_design_apis/drfx-forensics/drfx/utils/imageforensics"
        )
        os.chdir(wpath)

        output_string = subprocess.check_output(["python", "foreimg.py"] + flag + file_path, shell=False)
        after_output_string = output_string.decode("utf-8").strip()

        validated_data["image"] = outputimgpath
        validated_data["forensics_data_text"] = after_output_string
        forensicsdata = ForensicsData.objects.create(**validated_data)

        return forensicsdata