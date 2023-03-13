from django.contrib import admin

from . import models

# TODO: criar docstrings pra explicar melhor (nao so aqui, mas no model também)


class IsCompleteListFilter(admin.SimpleListFilter):
    #
    # OBS 1: É o parametro usado na URL do Browser com base nos lookups definidos.
    # no caso abaixo, a url ficaria algo como: admin/app_name/model_name/?is_complete=1 ou .../?is_complete=0

    # OBS 2: Eu só usei os numeros das primeiras posições em string ("1" e "0") pra ficar mais consistente e
    # facilitar leitura, visto que a segunda posição das tuplas sempre é uma string, pois é a representação
    # humana que irá aparecer no frontend da interface de Admin, então optei por manter todos os valores das
    # tuplas como string. Mas fiz o teste e usando integers 0 e 1 no lugar produz o mesmo resultado.

    title = "Is Complete"
    parameter_name = "is_complete"  # OBS 1

    def lookups(self, request, model_admin):
        return (
            ("0", "No"),
            ("1", "Yes"),
        )  # OBS 2

    def queryset(self, request, queryset):
        if self.value() == "1":
            return queryset.complete()
        elif self.value() == "0":
            return queryset.exclude(
                pk__in=queryset.complete().values_list("pk", flat=True)
            )


@admin.register(models.TodoList)
class TodoListAdmin(admin.ModelAdmin):
    """

    OBS 1: pra ao inves de mostrar "False" ou "True" na listagem, mostrar um icone

    OBS 2: no caso isso aqui se fosse um metodo do model, pra transformar em um icone eu teria que definir algo no model TODO: pesquisar como fazer isso

    OBS 3:

    nao precisa pois o model ja tem um metodo "is_complete", e o list_display busca nessa ordem: um callable ou atributo de TodoListAdmin (a classe Admin em que esta presente)
    ou entao um atributo ou metodo de todo.TodoList (o model em que a classe Admin esta registrada) entao no caso como o model ja possui um metodo is_complete, esse daqui é redundante
    percebi isso quando deu esse erro: The value of 'list_display[1]' refers to 'is_complete', which is not a callable, an attribute of 'TodoListAdmin', or an attribute or method on 'todo.TodoList'.
    TODO: Estudar mais isso, fazer testes criando um callable, dps um atributo dessa classe e por aí vai testando todas as opções
    """

    list_display = ("title", "is_complete")
    list_filter = (IsCompleteListFilter,)

    # def is_complete(self, obj):
    #     # OBS 3
    #     return obj.is_complete()

    # is_complete.boolean = True  # OBS 1 e OBS 2


@admin.register(models.TodoTask)
class TodoTaskAdmin(admin.ModelAdmin):
    pass
