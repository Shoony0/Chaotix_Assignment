from typing import Dict
from rest_framework.decorators import api_view
from text_to_game_ai.tasks import text_to_game_ai_task
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

def run_n_task_parallel(prompt_data_list: Dict):
    task_ids = []
    for prompt_data in prompt_data_list:
        task = text_to_game_ai_task.delay(prompt_data)
        task_ids.append(str(task.id))
    return task_ids

@api_view(["POST"])
def text_to_game_ai(request):
    task_ids = run_n_task_parallel(request.data) 
    return Response({
        "task_ids": task_ids,
        "message": f"{len(task_ids)} tasks is running parallel into background",
    }, status.HTTP_200_OK)
