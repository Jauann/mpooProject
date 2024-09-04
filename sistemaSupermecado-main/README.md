### MeGestor

O MeGestor disponibiliza uma API RESTfull que permite o acesso aos módulos do sistema para o gerenciamento do super mercado NOME_FICTICIO.

Recursos disponíveis via API:
* Dados da empresa
* Ajuste de estoque
* Vendas
* Relatórios de vendas

#### Frameworks e dependências
Para a construção da API utilizamos o framework FastAPI, feito em python, que nos disponibiliza toda a estrutura básica para o desenvolvimento do sistema

#### Estrutura da aplicação
A estutura da aplicação segue o modelo MVC, pois o mesmo facilita a implementação e permite uma modulariação que é benefica para debugar e alterar suas
funções sem que a mesma provoque interferência nas demais camadas da aplicação.

#### URLs de acesso
Os endpoint da API seguem um padrão bastante simple:

As requisições para API devem seguir o seguinte padrão:

#### Métodos de requesição
GET - Retorna informações de um ou mais registros
POST - Utilizado para criar um novo registro
PUT - Atualiza dados de um registro
DELETE - Deleta dados de um registro

#### Respostas
200 - Requesição executada com sucesso
400 - Erro de validação ou campos informados não existem no sistema
401 - Dados inválidos
404 - Registro pesquisado não encontrado
405 - Método não implementado
