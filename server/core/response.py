from datetime import datetime
from typing import Any

from fastapi.responses import JSONResponse
from pydantic import BaseModel


class ResponseJSON:
    @staticmethod
    def _serialize(data: Any) -> Any:
        if isinstance(data, datetime):
            return data.isoformat()
        elif isinstance(data, dict):
            return {k: ResponseJSON._serialize(v) for k, v in data.items()}
        elif isinstance(data, list):
            return [ResponseJSON._serialize(item) for item in data]
        return data

    @staticmethod
    def failure(status_code: int, message: str):
        return JSONResponse({
            'status': 'failure',
            'message': message
        }, status_code=status_code)

    @staticmethod
    def successful(status_code: int, data: Any):
       if isinstance(data, BaseModel):
            data = data.model_dump()
            data = ResponseJSON._serialize(data)
       elif isinstance(data, list):
            data = [ResponseJSON._serialize(item.model_dump() if isinstance(item, BaseModel) else item) for item in data]
       return JSONResponse({
            'status': 'success',
            'data': data
        }, status_code=status_code)
