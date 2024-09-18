import requests
from requests import Response


class PurchaseController():
    URL = 'http://localhost:5000/api/v1/history/'

    def get(self) -> Response:
        response = requests.get(self.URL)
        return response
