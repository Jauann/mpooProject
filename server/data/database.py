import json
import os
from typing import Any


class Database:
    @staticmethod
    def _write(file_path: str, data: dict[Any, Any]) -> bool:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        return True

    @staticmethod
    def _read(file_path: str) -> dict[Any, Any]:
        if not os.path.exists(file_path):
            Database._write(file_path=file_path, data={'data': {}})
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
        except json.JSONDecodeError:
            data = {'data': {}}
            Database._write(file_path=file_path, data=data)
        if 'data' not in data or data['data'] is None:
            data['data'] = {}
            Database._write(file_path=file_path, data=data)
        return data
