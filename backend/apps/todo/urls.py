from django.urls import path, include

from .api.routers import todo_list_router, todo_task_router


api_urlpatterns = [
    path("", include(todo_list_router.urls)),
    path("", include(todo_task_router.urls)),
]

urlpatterns = [
    path("api/", include(api_urlpatterns)),
]
