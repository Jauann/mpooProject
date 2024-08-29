import json
from models.product import Produto

class ServicoEstoque:
    def __init__(self):
        self.produtos = {}
        self.caminho_dados = "dados_estoque.json"

    def adicionar_produto(self, produto):
        self.produtos[produto.id_produto] = produto
        self.salvar_dados()

    def obter_produto(self, id_produto):
        return self.produtos.get(id_produto)

    def reduzir_estoque(self, id_produto, quantidade):
        produto = self.obter_produto(id_produto)
        if produto:
            produto.reduzir_estoque(quantidade)
            self.salvar_dados()
        else:
            raise ValueError("Produto não encontrado no estoque.")

    def salvar_dados(self):
        dados = {
            "produtos": [
                {
                    "id_produto": produto.id_produto,
                    "nome": produto.nome,
                    "preco": produto.preco,
                    "estoque": produto.estoque
                } for produto in self.produtos.values()
            ]
        }
        with open(self.caminho_dados, 'w') as arquivo:
            json.dump(dados, arquivo, indent=4)
        print("Dados do estoque salvos com sucesso.")

    def carregar_dados(self):
        try:
            with open(self.caminho_dados, 'r') as arquivo:
                dados = json.load(arquivo)
                for item in dados["produtos"]:
                    produto = Produto(item["id_produto"], item["nome"], item["preco"], item["estoque"])
                    self.produtos[produto.id_produto] = produto
            print("[✅️] — Dados do estoque carregados com sucesso.")
        except FileNotFoundError:
            print("Arquivo de dados do estoque não encontrado. Nenhum dado carregado.")
