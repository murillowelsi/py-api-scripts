from src.api.api_requests import createUser, listUsers
from src.data.user_fixture import users

for user in users:
    createUser(user)

listUsers()