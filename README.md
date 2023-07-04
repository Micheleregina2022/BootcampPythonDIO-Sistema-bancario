# Bootcamp *Python Developer* na **Digital Innovation One (DIO)**


## Objetivo Geral
Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato.

## Desafio

Fomos contratados por um grande banco para desenvolver o seu novo sistema. Esse 
banco deseja modernizar suas operações e para isso escolheu a linguagem Python. 
Para a primeira versão do sistema devemos implementar apenas 3 operações: depósito, saque e extrato.

### Operação de Depósito

Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, 
dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos 
devem ser armazenados em uma variável e exibidos na operação de extrato.

### Operação de Saque

O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. 
Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o 
dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

### Operação de Extrato

Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo
atual da conta. Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações.
Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo:
1500.45 = R$ 1500.45


*Desafio proposto por:*  
Guilherme Arthur de Carvalho  

@decarvalhogui


## Meu Código:

Criei uma classe chamada **Banco** para representar o sistema bancário. Ela possui as propriedades *saldo, depositos e saques*,
que são inicializadas vazias no construtor.

A operação de ***depositar()*** recebe um valor e verifica se é positivo antes de adicionar ao saldo e à lista de depósitos.

A operação de ***sacar()*** verifica se o valor é positivo, se o número de saques diários é inferior a 3, se o valor do saque é menor ou igual a 500 
e se há saldo suficiente antes de realizar o saque. Caso contrário, exibe uma mensagem de erro.

A operação de ***extrato()*** exibe uma listagem dos depósitos e saques realizados, seguidos do saldo atual. Se não houver movimentações, exibe uma
mensagem indicando que não foram realizadas movimentações.

No exemplo de uso, criei uma instância do objeto ***Banco*** chamada *banco* e realizei algumas operações, como depósitos e saques. Em seguida, 
foi exibido o extrato com o método **extrato()**.

#### Recursos utilizados:
 * classes
 * métodos
 * condicionais
 * formatação de strings
