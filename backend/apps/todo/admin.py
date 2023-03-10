from django.contrib import admin

from . import models


# TODO: Adicionar maneira de filtrar no admin pelas listas e tarefas que
# ja estao completas. É algo no list_filter, tenho certeza, só nao sei
# como faz pois nao da pra usar property, mas nao sei se vale a pena
# fazer um annotate no get_queryset do manager, ficaria estranho pois
# eu ja tenho um metodo complete() no meu Queryset personalizado...
# enfim, ver isso depois
@admin.register(models.TodoList)
class TodoListAdmin(admin.ModelAdmin):
    pass


@admin.register(models.TodoTask)
class TodoTaskAdmin(admin.ModelAdmin):
    pass
