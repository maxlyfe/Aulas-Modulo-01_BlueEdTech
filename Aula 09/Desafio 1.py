# Desafio: Faça um programa que ajude um jogador da MEGA SENA a criar
# palpites.O programa vai perguntar quantos jogos serão gerados e vai sortear 6
# números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.


# import random -> Importa a biblioteca completa

from random import randint # -> Importa apenas uma função da biblioteca

lista=[]
lista2=[]  #-> criei 3 listas para poder guardars os valores
lista3=[]

jogo = 6 # -> defini que os jogos tem que ter 6 valores diferentes
numeros = 0 # -> gerando variaveis com valor 0 para poder criar um contador
quantidade_listas = 0 # -> gerando variaveis com valor 0 para poder criar um contador

quantidade = int(input('Digite a quantidade de jogos que você deseja:\n')) #input para saber a quantidade de jogos que vão ser gerados.

while quantidade != quantidade_listas: 
    quantidade_listas +=1
    while numeros != jogo:
        #numero = random.randint(1,60) -> caso importe a biblioteca inteira.
        numero = randint(1,60) # -> comando usado para ativar apenas a função chamada
        if numero in lista:
          del()
        elif numero != lista:
            lista.append(numero)
            numeros += 1

    lista.sort()
    lista2.append(lista)
    
    numeros=0
    lista=[]
print(lista2)

