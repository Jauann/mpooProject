from controller.stock import StockController
from view.view import View


class StockView(View):
    OPT_SHOW = 1
    OPT_ADD = 2
    OPT_REMOVE = 3
    OPT_UPDATE = 4
    OPT_BACK = 5
    MIN_OPT = OPT_SHOW
    MAX_OPT = OPT_BACK

    MSG_SHOW = ' [1] — Exibir produtos 🏷️'
    MSG_ADD = ' [2] — Adicionar produtos 📝'
    MSG_REMOVE = ' [3] — Remover produto ❌'
    MSG_UPDATE = ' [4] — Alterar produto 📌'
    MSG_BACK = ' [5] - Voltar ao menu principal ↻'

    def __init__(self, title: str = 'Estoque') -> None:
        super().__init__(title)
        self.controller = StockController()

    def show_product(self, product: dict):
        print(f'ID: {product["id"]} \n| Nome: {product["name"]} \n| Preço: {product["price"]} \n| Quantidade: {product["quantity"]}\n')

    def show_products(self):
        try:
            response = self.controller.get()
            data = response.json()
            if response.status_code == 200:
                print('———————————————————————— [Lista de Produtos] ————————————————————————')
                for p in data['data']:
                    self.show_product(product=p)
            else:
                self.message_error(message=data['message'])
        except Exception:
            self.message_error(message='Não foi possível exibir os produtos...')

    def add_products(self):
        print('———————————————————————— [Adicionar Produtos] ————————————————————————')
        data = {'products': []}
        while True:
            name = self.custom_input(message='Nome: ', type=str)
            price = self.custom_input(message='Preço: ', type=float)
            quantity = self.custom_input(message='Quantidade: ', type=int)
            if self.confirm_input(message='Confirmar') == True:
                data['products'].append({'name': name, 'price': price, 'quantity': quantity})
            else:
                continue
            if self.confirm_input(message='Adionar um outro produto?') == False:
                break
        try:
            response = self.controller.create(data=data)
            data = response.json()
            if response.status_code == 201:
                print('\n————————————————————————[ Produto adicionado com sucesso ]————————————————————————')
                [self.show_product(product=p) for p in  data['data']]
            elif response.status_code == 422:
                self.message_error(message=data['detail'][0]['msg'])
            else:
                raise Exception
        except:
            self.message_error(message='Não foi possível adicionar os produtos...')

    def remove_product(self):
        print('———————————————————————— [Remover Produto] ————————————————————————')
        while True:
            id = self.custom_input(message='ID: ', type=str)
            if self.confirm_input(message='Confirmar') == False:
                continue
            try:
                response = self.controller.remove_by_id(id=id)
                data = response.json()
                if response.status_code == 204:
                    print('Produto deletado com sucesso')
                elif response.status_code == 404:
                    self.message_error(message=data['message'])
                else:
                    raise Exception
            except Exception:
                self.message_error(message='Não foi possível remover o produto...')
            if self.confirm_input(message='sair') == True:
                break
        

    def update_product(self):
        print('———————————————————————— [Atualizar Produto] ————————————————————————')
        while True:
            try:
                id = self.custom_input(message='ID: ', type=str)
                product = self.controller.get_by_id(id)
                data = product.json()
                if product.status_code == 200:
                    product = data['data']
                    if self.confirm_input(message='Alterar nome') == True:
                        name = self.custom_input(message='Nome: ', type=str)
                        product['name'] = name
                    if self.confirm_input(message='Alterar preço') == True:
                        price = self.custom_input(message='Preço: ', type=float)
                        product['price'] = price
                    if self.confirm_input(message='Alterar quantidade') == True:
                        quantity = self.custom_input(message='Quantidade: ', type=int)
                        product['quantity'] = quantity
                    response = self.controller.update_by_id(id, {'product': product})
                    data = response.json()
                    if response.status_code == 200:
                        print('\n* [Produto alterado com sucesso]')
                        self.show_product(product=data['data'])
                    elif response.status_code == 422:
                        self.message_error(message=data['detail'][0]['msg'])
                elif product.status_code == 404:
                    self.message_error(message=data['message'])
                else:
                    raise Exception
                if self.confirm_input(message='sair') == True:
                    break
            except:
                self.message_error(message='Não foi possível alterar o produto...')

    def render(self) -> None:
        while True:
            super().render()
            print(self.MSG_SHOW)
            print(self.MSG_ADD)
            print(self.MSG_REMOVE)
            print(self.MSG_UPDATE)
            print(self.MSG_BACK)
            opt = self.menu_select_option(max_opt=self.MAX_OPT, min_opt=self.MIN_OPT)

            if opt == self.OPT_SHOW:
                self.clear()
                self.show_products()
                self.enter_to_continue()
            elif opt == self.OPT_ADD:
                self.add_products()
                self.enter_to_continue()
            elif opt == self.OPT_REMOVE:
                self.remove_product()
            elif opt == self.OPT_UPDATE:
                self.update_product()
            else:
                return
