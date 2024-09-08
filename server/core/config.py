import os
from pathlib import Path


class Config:
    ORIGIN = 'http://localhost:5000'
    HOST = 'localhost'
    PORT = 5000
    DEBUG = True
    RELOAD = True
    LOG_LEVEL = 'info'
    DATA_FOLDER = os.path.join(Path(__file__).parent.parent, 'data')
    PRODUCTS_FILE = 'products.json'
    PURCHASES_FILE = 'purchases.json'
