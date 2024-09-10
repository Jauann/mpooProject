from view.purchase_history import PurchaseView
from view.view import View
from view.stock import StockView
from controller.order import OrderController


class OrderView(View):
    def __init__(self, title: str = '') -> None:
        super().__init__(title)
        self.controller = OrderController()
        self.stock_view = StockView()
        self.history_view = PurchaseView()

    def render(self) -> None:
        self.clear()
        self.stock_view.show_products()
        products = {'orders': []}
        print('[ Selecione os produtos acima ]')
        while True:
            product_id = self.custom_input(message='ID do produto: ', type= str)
            quantity = self.custom_input(message='Quantidade: ', type=int)
            print(f' * ID do produto {product_id}')
            print(f' * Quantidade: {quantity}')
            if self.confirm_input(message='Confirmar') == True:
                products['orders'].append({'product_id': product_id, 'quantity': quantity})
            else:
                continue
            if self.confirm_input(message='Adionar um outro produto?') == False:
                break
        try:
            response = self.controller.post(data=products)
            data = response.json()
            if response.status_code == 201:
                print('\n————————————————————————[ Comprovante de compra ]————————————————————————')
                self.history_view.show_purchase_history(data=data['data'])
                print('Tenha um bom dia!')
            else:
                self.message_error(message='Não foi possível efetuar a operação...')
        except:
            self.message_error(message='Não foi possível efetuar a operação...')
