import os
import uuid
from django.db import models

# Create your models here.

def file_location(instance, filename):
    file_path = os.path.join("generate_images", instance.title.replace(" ", "_"), filename)
    return file_path

class TextToImage(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    title = models.CharField(max_length=200)
    image_file = models.ImageField(upload_to=file_location, null=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.id}: {self.title}"