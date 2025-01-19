from rest_framework import serializers
from text_to_game_ai.models import TextToImage
from drf_extra_fields.fields import Base64ImageField

class ImageBase64Serilizer(serializers.ModelSerializer):
    image_file = Base64ImageField(required=False)
    class Meta:
        model = TextToImage
        fields = ["title", "image_file"]