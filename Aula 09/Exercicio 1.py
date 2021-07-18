# #01 - Crie um programa onde o usuário possa digitar vários valores numéricos e
# cadastre-os em uma lista. Caso o número já esteja lá dentro, ele não será
# adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem
# crescente.

lista = []

while True:
    r=(int(input('Digite o valor que será adicionado na lista:\n')))
    if r in lista:
        del()
    elif r != lista:
        lista.append(r)
    
    c= input('Deseja continuar adicionado valores? Sim/Não:\n').capitalize().format(' ','').replace('a','ã')
    if c=='Não':
        break
lista.sort()


print(lista)