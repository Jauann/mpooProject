from typing import Annotated

from api.controller.product import ProductController
from api.model.product import ProductModel
from api.model.product import ProductOut
from core.error import ErrorNotFound
from core.response import ResponseJSON
from fastapi import APIRouter
from fastapi import Body
from fastapi import status

router = APIRouter(prefix='/product')

product_controller = ProductController()


@router.get('/{id}', response_model=ProductOut, status_code=status.HTTP_200_OK)
async def get(id: str):
    try:
        product = product_controller.search_by_id(id)
        return ResponseJSON.successful(status_code=status.HTTP_200_OK, data=product)
    except ErrorNotFound as e:
        return ResponseJSON.failure(status_code=e.error_code, message=e.message)
    except Exception:
        return ResponseJSON.failure(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, message="An unexpected error occurred.")


@router.post('/', response_model=ProductOut, status_code=status.HTTP_201_CREATED)
async def create(product: Annotated[ProductModel, Body(embed=True)]):
    try:
        new_product = product_controller.create(product)
        return ResponseJSON.successful(status_code=status.HTTP_201_CREATED, data=new_product)
    except Exception:
        return ResponseJSON.failure(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, message="An unexpected error occurred.")


@router.put('/{id}', response_model=ProductOut, status_code=status.HTTP_200_OK)
async def update(id: str, product: Annotated[ProductModel, Body(embed=True)]):
    try:
        updated_product = product_controller.update(id, product)
        return ResponseJSON.successful(status_code=status.HTTP_200_OK, data=updated_product)
    except ErrorNotFound as e:
        return ResponseJSON.failure(status_code=e.error_code, message=e.message)
    except Exception:
        return ResponseJSON.failure(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, message="An unexpected error occurred.")


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete(id: str):
    try:
        product_controller.remove(id)
    except ErrorNotFound as e:
        return ResponseJSON.failure(status_code=e.error_code, message=e.message)
    except Exception:
        return ResponseJSON.failure(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, message="An unexpected error occurred.")
