from uuid import uuid4

from django.db import models
from django.conf import settings


USER_MODEL_STRING = settings.AUTH_USER_MODEL


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)


class TodoListQueryset(models.QuerySet):
    def complete(self):
        """
        Retorna somente as listas de tarefas concluidas. Listas "concluidas", são aquelas em que todos os
        objetos de TodoTask atrelados à mesma possuem o atributo "complete" com valor booleano igual a True.

        ___
        Passo a passo utilizado para resolver o problema:

            Passo 1 => Contar quantas tarefas a lista possui.

            Passo 2 => Contar quantas dessas tarefas estão concluidas. # (Um simples Count com parametro filter usando um Q() object
            deu conta do recado, achei que ia usar Subquery com OuterRef ou coisa do tipo)

            Passo 3 => Realizar filtragem buscando as listas em que o numero de tarefas concluidas é igual ao numero total de tarefas.
            (Pois significa que todas estao concluidas)

            Passo 4 => Retornar o queryset resultante do filtro realizado no passo 3.

        ___
        PS: Abaixo, onde tiver "task" (nos models.Count()) é pq to usando o valor do related_query_name
        """

        complete_queryset = self.alias(
            number_of_tasks=models.Count("task"),  # Passo 1
            number_of_complete_tasks=(
                models.Count("task", filter=models.Q(task__complete=True))
            ),  # Passo 2 (Ler "OBS 1")
        )

        complete_queryset = complete_queryset.filter(
            number_of_tasks=models.F("number_of_complete_tasks")  # Passo 3
        )

        return complete_queryset  # Passo 4

        # OBS 1: Pesquisar melhor pq isso funciona, achei que ao inves de task__complete ia precisar algo do tipo "F(task)__complete" sla
        # ou seja, nao entendi muito bem essa questao do filter passando um Q() object.


class TodoListManager(models.Manager):
    #
    def get_queryset(self):
        return TodoListQueryset(self.model, using=self._db)

    def complete(self):
        return self.get_queryset().complete()


class TodoList(BaseModel):
    #
    # managers

    objects = TodoListManager()

    # fields

    title = models.CharField(max_length=250)
    description = models.TextField()

    # relationships

    owner = models.ForeignKey(
        USER_MODEL_STRING,
        on_delete=models.CASCADE,
        related_name="todo_lists",  # pesquisar melhor maneira de nomear related_name quando o nome é composto
        related_query_name="todo_list",
    )

    # methods

    def get_tasks(self):
        return self.tasks.all()

    def __str__(self):
        return self.title


class TodoTaskQueryset(models.QuerySet):
    def complete(self):
        """
        Retorna somente as tarefas concluidas. Tarefas "concluidas", são aquelas que possuem
        o atributo "complete" com valor booleano igual a True.
        """
        return self.filter(complete=True)


class TodoTaskManager(models.Manager):
    #
    def get_queryset(self):
        return TodoTaskQueryset(self.model, using=self._db)

    def complete(self):
        return self.get_queryset().complete()


class TodoTask(BaseModel):
    #
    # managers

    objects = TodoTaskManager()

    # fields

    title = models.CharField(max_length=250)
    complete = models.BooleanField(default=False)

    # relationships

    todo_list = models.ForeignKey(
        TodoList,
        on_delete=models.CASCADE,
        related_name="tasks",
        related_query_name="task",
    )

    # methods

    def __str__(self):
        return self.title


"""
from apps.todo.models import TodoList
complete = TodoList.objects.complete()
for todo_list in complete:
    print(todo_list.__dict__)
"""
