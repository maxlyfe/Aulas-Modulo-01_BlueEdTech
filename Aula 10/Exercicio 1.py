# 1 - Crie uma lista composta que recebe 5 nomes e 5 idades de clientes, utilizando o for e o if,
# verifique quais clientes são maiores de idade e quais são menores de idade e mostre na tela
# a seguinte frase para cada um deles: 'Fulano é maior de idade' ou 'Fulana é menor de idade'
# e também quantos são maiores e quantos são menores de idade.
# lista=[]
# listaIdade=[]
# maior=[]
# menor=[]

# for i in range(3):
#     informação = input('Informe o seu nome:\n')
#     lista.append(informação)
#     informação2 = int(input('Informe a sua idade:\n'))
#     lista.append(informação2)
#     listaIdade.append(informação2)
#     if informação2 >= 18:
#         maior.append(informação)
#         maior.append(informação2)
#     elif informação2 < 18:
#         menor.append(informação)
#         menor.append(informação2)
# for n in lista:
#     print(f'')


# print(lista)
# print()
# print(listaIdade)
# print()
# print(maior)
# print()
# print(menor)

lista=[[],[]]

for i in range(5):
    nome=input('Informe seu nome:\n')
    lista[0].append(nome)
    idade=int(input('informe sua idade:\n'))
    lista[1].append(idade)
    
print(lista)