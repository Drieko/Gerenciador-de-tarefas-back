# meu_app/views.py
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Task

@require_http_methods(["GET"])
def get_tasks(request):
    tasks = Task.objects.all()
    return JsonResponse([task.to_dict() for task in tasks], safe=False)

@require_http_methods(["GET"])
def get_task(request, id):
    try:
        task = Task.objects.get(id=id)
        return JsonResponse(task.to_dict())
    except Task.DoesNotExist:
        return JsonResponse({"error": "Task not found"}, status=404)

@require_http_methods(["POST"])
def create_task(request):
    data = request.json()
    task = Task.objects.create(**data)
    return JsonResponse(task.to_dict())

@require_http_methods(["PUT"])
def update_task(request, id):
    try:
        task = Task.objects.get(id=id)
        data = request.json()
        task.update(**data)
        return JsonResponse(task.to_dict())
    except Task.DoesNotExist:
        return JsonResponse({"error": "Task not found"}, status=404)

@require_http_methods(["DELETE"])
def delete_task(request, id):
    try:
        task = Task.objects.get(id=id)
        task.delete()
        return JsonResponse({"message": "Task deleted"})
    except Task.DoesNotExist:
        return JsonResponse({"error": "Task not found"}, status=404)