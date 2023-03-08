from rest_framework.serializers import ModelSerializer

from ..models import TodoList, TodoTask


class TodoListSerializer(ModelSerializer):
    # TODO: Fazer o mesmo que fiz abaixo com TodoListSerializer() so que pra owner
    class Meta:
        model = TodoList
        fields = ("id", "title", "description", "owner")


class TodoTaskSerializer(ModelSerializer):
    #
    todo_list = TodoListSerializer()

    class Meta:
        model = TodoTask
        fields = ("id", "title", "complete", "todo_list")
