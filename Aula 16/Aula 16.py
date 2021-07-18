#Forca
from random import choice

quantidade_erros_atual = 0
quantidade_erros_jogo = 6 #representa Game-Over, já que na forca tem 6 chances.

palavras = ['lixeira','circo','pneu','maremoto','vendanal','alegremente']
letras_erradas = []
letras_certas = []

palavra = choice(palavras).lower()
palavra_exibicao = list('_'*len(palavra))
print('Bem-vindo(a) ao jogo da forca!!!')
print(f'Você pode cometer até {quantidade_erros_jogo-1} erros, ou seja, no erro número {quantidade_erros_jogo} você perde o jogo.')
print('Boa sorte! =)\n')
while quantidade_erros_atual < quantidade_erros_jogo and '_' in palavra_exibicao:
    print('Palavra: ', ' '.join(palavra_exibicao))
    print(f'Status: {quantidade_erros_atual} de {quantidade_erros_jogo} erros ')
    print(f'Letras erradas: {", ".join(letras_erradas)}')
    while letra in letras_erradas or letra in letras_certas:
        letra = input(f' Letra >>>{letra}<<< já foi utilizada. Por favor, informe outra letra.\n')
    if letra not in palavra:
        letras_erradas.append(letra)
        quantidade_erros_atual += 1
    else:
        letras_certas.append(letra)
        cont = 0
        while cont < len(palavra):
            if palavra[cont] == letra:
                palavra_exibicao[cont] = letra
            cont +=1
if '_' not in palavra_exibicao:
    print(f'Parabéns! Você ganhou o jogo, a palavra era {palavra}')
if quantidade_erros_atual == quantidade_erros_jogo:
    print(f'Você acabou de ser enforcado, a palavra era {palavra}.')