from rest_framework.routers import DefaultRouter

from .viewsets import TodoListViewSet, TodoTaskViewSet

todo_list_router = DefaultRouter()
todo_list_router.register(r"lists", TodoListViewSet, basename="api-lists")

todo_task_router = DefaultRouter()
todo_task_router.register(r"tasks", TodoTaskViewSet, basename="api-tasks")
