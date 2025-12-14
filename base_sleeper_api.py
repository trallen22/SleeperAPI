import requests

class BaseSleeperAPI:
    SLEEPER_BASE_ENDPOINT = "https://api.sleeper.app/"

    def __init__(self):
        pass

    @classmethod
    def callApi(cls, path: str):
        endpoint = f"{cls.SLEEPER_BASE_ENDPOINT}{path}"
        print(f"getting endpoint: {endpoint}")
        return requests.get(endpoint).json()