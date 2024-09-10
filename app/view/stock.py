from controller.stock import StockController
from view.view import View


class StockView(View):
    MIN_OPT = 1
    MAX_OPT = 5
    OPT_1 = ' [1] — Exibir produtos'
    OPT_2 = ' [2] — Adicionar produto'
    OPT_3 = ' [3] — Remover produto'
    OPT_4 = ' [4] — Alterar produto'
    OPT_5 = ' [5] - Voltar ao menu principal'

    def __init__(self, title: str = 'Estoque') -> None:
        super().__init__(title)
        self.controller = StockController()

    def show_products(self):
        try:
            response = self.controller.get()
            data = response.json()
            if response.status_code == 200:
                print('———————————————————————— [Lista de Produtos] ————————————————————————')
                for p in data['data']:
                    print(f'ID: {p['id']} \n| Nome: {p['name']} \n| Preço: {p['price']} \n| Quantidade: {p['quantity']}\n')
            else:
                self.message_error(message=data['message'])
        except Exception as e:
            self.message_error(message='Não foi possível exibir os produtos...')

    def render(self) -> None:
        while True:
            super().render()
            print(self.OPT_1)
            print(self.OPT_2)
            print(self.OPT_3)
            print(self.OPT_4)
            print(self.OPT_5)
            opt = self.menu_select_option(max_opt=self.MAX_OPT, min_opt=self.MIN_OPT)

            if opt == 1:
                self.show_products()
                self.enter_to_continue()
            if opt == self.MAX_OPT:
                return
