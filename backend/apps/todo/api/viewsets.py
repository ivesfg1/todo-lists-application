from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import TodoListSerializer, TodoTaskSerializer
from ..models import TodoList, TodoTask


class TodoListViewSet(ModelViewSet):
    #
    serializer_class = TodoListSerializer
    queryset = TodoList.objects.all()

    @action(methods=["GET"], detail=False)
    def complete(self, request):
        #
        # TODO: melhorar isso aqui

        # Talvez seja melhor um queryparameter ao inves de um url parameter
        # Com isso, é necessario consumir: /api/lists/complete
        # acho que seria melhor: /api/lists?complete=true

        queryset = self.queryset.complete()
        queryset = self.filter_queryset(queryset)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class TodoTaskViewSet(ModelViewSet):
    #
    serializer_class = TodoTaskSerializer
    queryset = TodoTask.objects.all()

    @action(methods=["GET"], detail=False)
    def complete(self, request):
        #
        # TODO: melhorar isso aqui

        # Talvez seja melhor um queryparameter ao inves de um url parameter
        # Com isso, é necessario consumir: /api/tasks/complete
        # acho que seria melhor: /api/tasks?complete=true

        queryset = self.queryset.complete()
        queryset = self.filter_queryset(queryset)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
