### Exercício 2- Crie um programa, utilizando dicionário, que simule a baixa de estoque 
# das vendas de um supermercado. Não esqueça de fazer as seguintes validações:​

# Produto Indisponível​
# Produto Inválido​
# Quantidade solicitada não disponível ​

# O programa deverá mostrar para o cliente a quantidade de itens comprados e o total.

produtos = {'Agua':15, 'Batata':60, 'Coca-Cola':8, 'Pokebolas':23, 'Biscoito':2, 'Figado':0}
compra = {}
while True:
    pedido = input('O que você desejá?\n')
    if pedido in produtos.key():
        quantidade=int(input('Quantos(as) você deseja? \n'))
        if quantidade in produtos.values():
        