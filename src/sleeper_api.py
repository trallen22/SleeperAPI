import requests

SLEEPER_BASE_ENDPOINT = "https://api.sleeper.app/"

def callApi(path: str):
    endpoint = f"{SLEEPER_BASE_ENDPOINT}{path}"
    print(f"getting endpoint: {endpoint}")
    return requests.get(endpoint).json()