import requests
from requests import Response


class OrderController:
    URL = 'http://localhost:5000/api/v1/order/'

    def __init__(self) -> None:
        pass

    def post(self, data: dict) -> Response:
        response = requests.post(self.URL, json=data)
        return response
