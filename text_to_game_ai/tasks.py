from typing import Dict
from celery import shared_task
import requests
from text_to_game_ai import serializers


@shared_task
def text_to_game_ai_task(json_data: Dict):
    url = "https://api.stability.ai/v1/generation/stable-diffusion-xl-1024-v1-0/text-to-image"

    body = {
        "steps": 40,
        "width": 1024,
        "height": 1024,
        "seed": 0,
        "cfg_scale": 5,
        "samples": 1,
        "text_prompts": [
            {
            "text": json_data["text"],
            "weight": 1
            }
        ],
    }

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer sk-mCKRXpwmkmUYt8rnWjluZnqf8eDex4yvFT24Ab0E3sYUbskS",
    }

    response = requests.post(
        url,
        headers=headers,
        json=body,
    )

    if response.status_code != 200:
        raise Exception("Non-200 response: " + str(response.text))

    data = response.json()

    for image in data["artifacts"]:
        data = {
            "title": json_data["text"],
            "image_file": image["base64"],
        }
        serializer = serializers.ImageBase64Serilizer(data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            return serializer.errors
