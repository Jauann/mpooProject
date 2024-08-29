from fastapi.responses import JSONResponse

class ResponseJSON:
    @staticmethod
    def failure(status_code: int, message: str):
        return JSONResponse({
            'status': 'failure',
            'message': message 
        }, status_code = status_code)

    @staticmethod
    def successfull(status_code: int, data: any):
        return JSONResponse({
            'status': 'success',
            'data': data 
        }, status_code = status_code)
