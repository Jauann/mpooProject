from fastapi import APIRouter
from fastapi import status

router = APIRouter(prefix='/history')

@router.get('/', status_code=status.HTTP_200_OK)
async def get():
    return
