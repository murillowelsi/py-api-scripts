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
        )
        usersList = response.json()
        for user in usersList:
            print(user["name"])
        print(f"API status code: {response.status_code}")
    except Exception as e:
        print(e)


def createUser(body):
    try:
        print(f"Token generated for the user: {body['name']}")
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
