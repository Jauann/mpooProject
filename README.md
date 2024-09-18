<a id="readme-top"></a>

<br />
<div align="center">
  <a href="https://github.com/othneildrew/Best-README-Template">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">MeGestor API</h3>
  <p align="center">
    Sistema de gerenciamento de supermercado
  </p>
</div>

### Sobre o projeto

O MeGestor disponibiliza uma API RESTfull que permite o acesso aos módulos do sistema para o gerenciamento do super mercado NOME_FICTICIO.

Recursos disponíveis via API:
* [**Dados da empresa**]
* [**juste de estoque**]
* [**Vendas**]
* [**elatórios de vendas**]

#### Frameworks e dependências
Para a construção da API utilizamos o framework FastAPI, feito em python, que nos disponibiliza toda a estrutura básica para o desenvolvimento do sistema

#### Estrutura da aplicação
A estutura da aplicação segue o modelo MVC, pois o mesmo facilita a implementação e permite uma modulariação que é benefica para debugar e alterar suas
funções sem que a mesma provoque interferência nas demais camadas da aplicação.

#### URLs de acesso
Os endpoints da API seguem um padrão bastante simple:

##### Ajuste de estoque
```
megestor/api/v1/estoque
```

##### Vendas
```
megestor/api/v1/produtos
```

##### Relatórios de vendas
```
megestor/api/v1/relatorios
```

#### Métodos de requesição
| Método | Descrição |
|---|---|
| `GET` | Retorna informações de um ou mais registros. |
| `POST` | Utilizado para criar um novo registro. |
| `PUT` | Atualiza dados de um registro ou altera sua situação. |
| `DELETE` | Remove um registro do sistema. |

#### Respostas
| Código | Descrição |
|---|---|
| `200` | Requisição executada com sucesso (success).|
| `400` | Erros de validação ou os campos informados não existem no sistema.|
| `401` | Dados de acesso inválidos.|
| `404` | Registro pesquisado não encontrado (Not found).|
| `405` | Método não implementado.|

