from view.order import OrderView
from view.purchase_history import PurchaseView
from view.stock import StockView
from view.view import View


class AppView(View):
    MIN_OPT = 1
    MAX_OPT = 4
    OPT_1 = ' [1] — Manusear estoque 📦'
    OPT_2 = ' [2] — Realizar venda 🛒'
    OPT_3 = ' [3] — Exibir histórico de vendas 📝'
    OPT_4 = ' [4] — Sair 👋'

    def __init__(self, title: str = 'menu') -> None:
        super().__init__(title)
        self.purchase = PurchaseView()
        self.order = OrderView()
        self.stock = StockView()

    def render(self) -> None:
        self.clear()
        while True:
            super().render()
            print(self.OPT_1)
            print(self.OPT_2)
            print(self.OPT_3)
            print(self.OPT_4)
            opt = self.menu_select_option(
                max_opt=self.MAX_OPT, min_opt=self.MIN_OPT)

            if opt == 1:
                self.stock.render()
            elif opt == 2:
                self.order.render()
                self.enter_to_continue()
            elif opt == 3:
                self.show_spinner(msg='Carrendo histórico de vendas')
                self.purchase.render()
                self.enter_to_continue()
            else:
                exit(0)
