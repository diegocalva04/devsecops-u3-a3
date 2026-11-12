import requests


def fetch_data(url):
    # Vulnerabilidad SAST: credencial hardcodeada.
    api_key = "12345-SUPER-SECRET-KEY"
    response = requests.get(f"{url}?key={api_key}")
    return response.json()


def run_user_code(user_code):
    # Vulnerabilidad SAST de severidad alta: ejecucion arbitraria.
    exec(user_code)


def health_check():
    return {"status": "ok"}
