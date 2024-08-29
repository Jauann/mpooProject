from fastapi import APIRouter, status
from api.controller.stock import StockController
from api.model.product import ProductOut
from core.response import ResponseJSON

router = APIRouter(prefix='/stock')

stockController = StockController()

@router.get('/', response_model=list[ProductOut], status_code=status.HTTP_200_OK)
async def get():
    data = stockController.get_all()
    return ResponseJSON.successfull(status_code=status.HTTP_200_OK, data=data)

@router.post('/', response_model=list[ProductOut], status_code=status.HTTP_201_CREATED)
async def create(products: list[ProductOut]):
    print(products)
    return ResponseJSON.successfull(status_code=status.HTTP_200_OK, data=products)

@router.delete('/', status_code=status.HTTP_204_NO_CONTENT)
async def delete(products: list[ProductOut]):
    pass
