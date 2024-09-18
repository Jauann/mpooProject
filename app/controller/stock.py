import requests
from requests import Response


class StockController:
    URL = 'http://localhost:5000/api/v1/stock/'
    URL_PRODUCT = 'http://localhost:5000/api/v1/product/'

    def get(self) -> Response:
       response = requests.get(self.URL)
       return response

    def get_by_id(self, id: str) -> Response:
        response = requests.get(f'{self.URL_PRODUCT}{id}')
        return response

    def create(self, data: dict) -> Response:
       response = requests.post(self.URL, json=data)
       return response

    def remove_by_id(self, id: str) -> Response:
        response = requests.delete(f'{self.URL_PRODUCT}{id}')
        return response

    def update_by_id(self, id: str, data: dict) -> Response:
        response = requests.put(f'{self.URL_PRODUCT}{id}', json=data)
        return response
