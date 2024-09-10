import requests
from requests import Response


class StockController:
    URL = 'http://localhost:5000/api/v1/stock/'

    def __init__(self) -> None:
        pass

    def get(self) -> Response:
       response = requests.get(self.URL)
       return response

    def get_by_id(self, id: str) -> Response:
       response = requests.get(self.URL, params=id)
       return response

    def create(self):
        pass

    def remove(self):
        pass

    def update(self):
        pass
