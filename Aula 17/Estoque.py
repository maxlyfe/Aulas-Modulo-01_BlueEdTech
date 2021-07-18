### Exercício 2- Crie um programa, utilizando dicionário, que simule a baixa de estoque 
# das vendas de um supermercado. Não esqueça de fazer as seguintes validações:​

# Produto Indisponível​
# Produto Inválido​
# Quantidade solicitada não disponível ​

# O programa deverá mostrar para o cliente a quantidade de itens comprados e o total.

itens_comprado = []
total_quantidade_geral = 0
estoque = {'coca':15,'chocolate':6,'batata':11, 'papel':13,'presunto':26}

continuar = input('Bem-vindo(a) ao Supermercado T3C5!. Deseja ir as compras? (s/n)\n').lower()

while continuar not in ['s','n']:
    continuar = input('Resposta não valida. Deseja ir as compras? (s/n)\n').lower()

while continuar == 's':
    print('Nossos produtos:')

    for i in estoque:
        if estoque(i)>0:
            print(i)

    produto = input('Qual produto você deseja comprar?\n')
    quantidade_atual = estoque.get(produto,-1)

    if quantidade_atual == -1:
        print('Produto Invalido.')
    elif quantidade_atual == 0:
        print('Produto indisponivel.')
    else:
        quantidade = int(input('Qual a quantidade desejada?\n'))
        if quantidade > quantidade_atual:
            print(f'Quantidade indisponivel. No momento apenas temos {quantidade_atual} em estoque.')
        else:
            estoque[produto] = quantidade_atual - quantidade
            if produto not in itens_comprado:
                itens_comprado.append(produto)
            total_quantidade_geral += quantidade
            print('Compra realizada com sucesso!!!')

    continuar = input('Deseja ir as compras? (s/n)\n').lower()
    while continuar not in ['s','n']:
        continuar = input('Resposta não valida. Deseja ir as compras? (s/n)\n').lower()
print('---Resumo da compra ---')
print(f'Quantidade de itens comprados: {len(itens_comprado)}')
print(f'Total de itens comprados: {total_quantidade_geral}')