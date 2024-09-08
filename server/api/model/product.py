from pydantic import BaseModel
from pydantic import Field


class ProductModel(BaseModel):
    name: str
    price: float = Field(gt=0, description='The price must be greater than zero')
    quantity: int = Field(gt=0, description='The quantity must be greater than zero')

class ProductOut(ProductModel):
    id: str

    def model_dump(self, *args, **kwargs):
        original_dict = super().model_dump(*args, **kwargs)
        return {'id': self.id, **original_dict}
