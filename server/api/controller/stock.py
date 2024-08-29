import os
import json
from core.config import Config

class StockController:
    def __init__(self):
        self.json_path = os.path.join(Config.PROJECT_FOLDER, Config.DATA_FOLDER, Config.DATA_FILE)

    def get_all(self) -> list[dict]:
        with open(self.json_path, 'r') as file:
            json_data = json.load(file)
        data_list = [{"id": key, **value} for key, value in json_data["data"].items()]
        return data_list

    def create(self):
        pass

    def delete(self):
        pass
