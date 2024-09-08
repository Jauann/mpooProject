from api.router import order
from api.router import product
from api.router import purchase_history
from api.router import stock
from fastapi import FastAPI


class App:
    PREFIX_V1 = '/api/v1'

    def __init__(self):
        self.app = FastAPI()
        self.include_routers()

    def start(self):
        return self.app

    def include_routers(self):
        self.app.include_router(prefix=self.PREFIX_V1, tags=["Product"], router=product.router)
        self.app.include_router(prefix=self.PREFIX_V1, tags=["Stock"], router=stock.router)
        self.app.include_router(prefix=self.PREFIX_V1, tags=["History"], router=purchase_history.router)
        self.app.include_router(prefix=self.PREFIX_V1, tags=["Order"], router=order.router)


app = App().start()
