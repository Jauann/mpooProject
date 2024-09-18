from datetime import datetime
from controller.purchase_history import PurchaseController
from view.view import View


class PurchaseView(View):
    def __init__(self, title: str = 'histórico de compras') -> None:
        super().__init__(title)
        self.controller = PurchaseController()

    def show_purchase_history(self, data: dict):
        print(f'ID da compra: {data["id"]}')
        print(f'Cliente: {data["client_id"]}')
        print(f'Pedidos: ', end='')
        [print(f' \n Nome: {p["product_name"]}\n Preço: R${float(p["product_price"]):.2f}\n Quantidade: {p["quantity"]}') for p in data["orders"]]
        date_obj = datetime.fromisoformat(data['date'])
        print(f'Data: {date_obj.date()} às {date_obj.time().strftime("%H:%M:%S")}')
        self.draw_line()
        print(f'total R$ {data["total_price"]}\n')

    def render(self):
        super().render()
        try:
            response = self.controller.get()
            data = response.json()
            if response.status_code == 200:
                for history in data['data']:
                    self.show_purchase_history(data=history)
            else:
                self.message_error(message=data['message'])
        except:
            self.message_error(message='Não foi possível recuperar os dados do histórico de compras...')

