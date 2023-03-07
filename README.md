# todo-lists-application

## Aplicação FullStack onde usuários podem se cadastrar e criar listas de tarefas.


## Tecnologias utilizadas:

- BackEnd desenvolvido em Python utilizando do framework Django e sua extensão Django Rest Framework para a criação da API.
- FrontEnd até então desenvolvido com HTML, CSS e Javascript puro, sem utilização de nenhum framework ou biblioteca externa, apenas manipulação direta do DOM.

## Requisitos:

### Autenticação:

- Um usuário deve poder se cadastrar no sistema;
- Um usuário deve poder realizar login no sistema;

### CRUD Listas de Tarefas:

- Um usuário deve poder visualizar suas listas de tarefas;
- Um usuário deve poder criar uma nova lista de tarefa, informando título e descrição;
- Um usuário deve poder editar uma lista de tarefas existente;
- Um usuário deve poder excluir uma lista de tarefas existente;

### CRUD Tarefas:

- Um usuário deve poder visualizar suas tarefas atreladas à uma lista de tarefas específica;
- Um usuário deve poder editar uma tarefa específica atrelada à uma lista de tarefas específica;
- Um usuário deve poder concluir uma tarefa específica atrelada à uma lista de tarefas específica;;
- Um usuário deve poder excluir uma tarefa específica atrelada à uma lista de tarefas específica;

### Diferenciais:

- Um usuário deve poder mover uma tarefa para outra lista de tarefas existente;
- Um usuário deve poder categorizar listas de tarefas para facilitar filtragem;
- Um usuário deve poder filtrar listas de tarefas pelo status de conclusão;
- Uma lista de tarefas se caracteriza como concluída quando todas as suas tarefas possuem status de concluído.

## Endpoints da API

### V1

- /lists/ (GET, POST);

- /lists/{list-id}/ (GET, PUT, PATCH, DELETE);

- /tasks/ (GET, POST);

- /tasks/{task-id}/ (GET, PUT, PATCH, DELETE);

### V2

- /lists/ (GET, POST);

- /lists/{list-id}/ (GET, PUT, PATCH, DELETE);

- /lists/{list-id}/tasks/ (GET, POST);

- /lists/{todo-list-id}/tasks/{task-id}/ (GET, PUT, PATCH, DELETE);
