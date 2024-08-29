from fastapi import FastAPI
from api.router import product, stock

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
