# 01 - Faça um programa que leia o peso de cinco pessoas. No final,
# mostre qual foi
# o maior e o menor peso lidos.

# lista = []
# in i is range(5)
#     lista.append((input('Informe o peso das pessoas:\n'))
#     resultado = som(lista)

# print(f'A soma de todos os valores é de {resultado}Kg')

lista = []

for i in range(5):
    lista.append(int(input('Digite o peso:\n')))
resultado = sum(lista)
print(f'A soma dos valore é de {resultado}Kg.')
