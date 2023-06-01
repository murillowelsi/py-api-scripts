import os
import requests
from dotenv import load_dotenv

if os.getenv("ENV"):
    env = os.getenv("ENV")
else:
    env = "local"

load_dotenv(f".env.{env}")

apiUrl = os.getenv("API_BASE_URL")
accessToken = os.getenv("ACCESS_TOKEN")


def listUsers():
    try:
        response = requests.get(
            f"{apiUrl}/users",
            headers={
                "Content-type": "application/json",
                "Authorization": f"Bearer {accessToken}",
            },
            params={
                "page": 1,
                "per_page": 100,
            },
        )
        usersList = response.json()
        for user in usersList:
            print(user["name"])
        print(f"API status code: {response.status_code}")
    except Exception as e:
        print(e)


def createUser(body):
    try:
        response = requests.post(
            f"{apiUrl}/users",
            json=body,
            headers={
                "Content-type": "application/json",
                "Authorization": f"Bearer {accessToken}",
            },
        )
        print(f"API status code: {response.status_code}")
    except Exception as e:
        print(e)


def listTodos():
    try:
        response = requests.get(
            f"{apiUrl}/todos",
            headers={
                "Content-type": "application/json",
                "Authorization": f"Bearer {accessToken}",
            },
            params={
                "page": 1,
                "per_page": 100,
            },
        )
        todosList = response.json()
        for todo in todosList:
            print(todo["title"])
        print(f"API status code: {response.status_code}")
    except Exception as e:
        print(e)


def createTodo(body):
    try:
        response = requests.post(
            f"{apiUrl}/todos",
            json=body,
            headers={
                "Content-type": "application/json",
                "Authorization": f"Bearer {accessToken}",
            },
        )
        print(f"API status code: {response.status_code}")
    except Exception as e:
        print(e)
