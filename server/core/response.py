from typing import Any

from fastapi.responses import JSONResponse
from pydantic import BaseModel


class ResponseJSON:
    @staticmethod
    def failure(status_code: int, message: str):
        return JSONResponse({
            'status': 'failure',
            'message': message
        }, status_code=status_code)

    @staticmethod
    def successful(status_code: int, data: Any):
       if isinstance(data, BaseModel):
            data = data.dict()
       elif isinstance(data, list):
            data = [item.dict() if isinstance(item, BaseModel) else item for item in data]
       return JSONResponse({
            'status': 'success',
            'data': data
        }, status_code=status_code)
