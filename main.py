from src.api.api_requests import createTodo, createUser, listUsers, listTodos
from src.data.user_fixture import users

# from src.data.todo_fixture import todos

for user in users:
    createUser(user)

# for todo in todos:
#     createTodo(todo)

listUsers()
listTodos()
