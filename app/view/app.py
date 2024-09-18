from view.order import OrderView
from view.purchase_history import PurchaseView
from view.stock import StockView
from view.view import View


class AppView(View):
    OPT_STOCK = 1
    OPT_BUY = 2
    OPT_HISTORY = 3
    OPT_EXIT = 4
    MIN_OPT = OPT_STOCK
    MAX_OPT = OPT_EXIT

    MSG_STOCK = ' [1] — Manusear estoque 📦'
    MSG_BUY = ' [2] — Realizar venda 🛒'
    MSG_HISTORY = ' [3] — Exibir histórico de vendas 📝'
    MSG_EXIT = ' [4] — Sair 👋'

    def __init__(self, title: str = 'menu') -> None:
        super().__init__(title)
        self.purchase = PurchaseView()
        self.order = OrderView()
        self.stock = StockView()

    def render(self) -> None:
        self.clear()
        while True:
            super().render()
            print(self.MSG_STOCK)
            print(self.MSG_BUY)
            print(self.MSG_HISTORY)
            print(self.MSG_EXIT)
            opt = self.menu_select_option(
                max_opt=self.MAX_OPT, min_opt=self.MIN_OPT)

            if opt == self.OPT_STOCK:
                self.stock.render()
            elif opt == self.OPT_BUY:
                self.order.render()
                self.enter_to_continue()
            elif opt == self.OPT_HISTORY:
                self.show_spinner(msg='Carrendo histórico de vendas')
                self.purchase.render()
                self.enter_to_continue()
            else:
                exit(0)
