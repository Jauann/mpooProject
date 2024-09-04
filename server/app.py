from api.router import product
from api.router import stock
from fastapi import FastAPI


class App:
    def __init__(self):
        self.app = FastAPI()
        self.include_routers()

    def start(self):
        return self.app

    def include_routers(self):
        self.app.include_router(prefix='/api/v1', tags=["Product"], router=product.router)
        self.app.include_router(prefix='/api/v1', tags=["Stock"], router=stock.router)


app = App().start()
