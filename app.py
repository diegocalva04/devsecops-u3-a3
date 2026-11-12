import os

import requests


def fetch_data(url):
    api_key = os.environ.get("API_KEY")
    response = requests.get(url, headers={"X-API-Key": api_key}, timeout=10)
    return response.json()


def run_user_code(user_code):
    raise ValueError("Ejecucion de codigo arbitrario no permitida")


def health_check():
    return {"status": "ok"}
