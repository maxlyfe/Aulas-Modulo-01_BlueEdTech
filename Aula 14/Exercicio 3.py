# 1.	Faça um programa com uma função chamada somaImposto.
# A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto
#  sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto.
#   A função “altera” o valor de custo para incluir o imposto sobre vendas.
def somaImposto(taxaImposto,custo):
    calculo = (taxaImposto/100)*custo + custo
    return calculo
taxa = 31
preco = float(input('Informe o valor do produto\nR$').replace(',','.'))
print(f'O valor do produto mais taxas é de {somaImposto(taxa,preco)}')