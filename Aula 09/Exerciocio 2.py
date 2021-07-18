#02 - Crie um programa que vai ler vários números e colocar em uma lista. Depois
# disso, crie duas listas extras que vão conter apenas os valores pares e os valores
# ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas
# geradas.

lista1 = []
lista2 = []
lista3 = []

while True:
    r=(int(input('Digite o valor que será adicionado na lista:\n')))
    if r in lista1:
        del()
    elif r != lista1:
        lista1.append(r)
    if r%2 == 0:
        lista2.append(r)
    elif r%2 != 0:
        lista3.append(r)
    c= input('Deseja continuar adicionado valores? Sim/Não:\n').capitalize().format(' ','').replace('a','ã')
    if c=='Não':
        break

print(lista1)
print()
print(lista2)
print()
print(lista3)
print()