import os
import json
import uuid
from api.model.product import ProductModel
from core.config import Config

class ProductController:
    def __init__(self):
        self.json_path = os.path.join(Config.PROJECT_FOLDER, Config.DATA_FOLDER, Config.DATA_FILE)

    def _write(self, data: dict) -> bool:
        with open(self.json_path, 'w') as file:
            json.dump(data, file, indent=4)
        return True

    def search_by_id(self, id: str) -> dict | None:
        with open(self.json_path, 'r') as file:
            json_data = json.load(file)
        return json_data['data'].get(id)

    def create(self, product: ProductModel) -> dict:
        with open(self.json_path, 'r') as file:
            json_data = json.load(file)
        id = str(uuid.uuid4())
        json_data['data'][id] =  {
            'name': product.name,
            'price': product.price,
            'quantity': product.quantity,
        }
        self._write(data=json_data)
        return json_data['data'][id]
        
    def update(self, id: str, product: ProductModel) -> bool:
        with open(self.json_path, 'r') as file:
             json_data = json.load(file)
        if id in json_data['data']: 
            json_data['data'][id] = {
                'name': product.name,
                'price': product.price,
                'quantity': product.quantity,
            }
            self._write(data=json_data)
            return json_data['data'][id]
        return None

    def remove(self, id: str) -> bool:
        with open(self.json_path, 'r') as file:
            json_data = json.load(file)
        if id in json_data['data']:
            del json_data['data'][id]
            return self._write(data=json_data)
        else:
            return False
