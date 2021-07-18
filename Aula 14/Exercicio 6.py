# 6.	Escreva uma função que, dado um número nota representando a 
# nota de um estudante, converte o valor de nota para um conceito (A, B, C, D, E e F).
def conceito (x):
    nota = 0
    if x >= 4.1:
        nota = 'E'
    if x >= 6.0:
        nota = 'D'
    if x >= 7.0:
        nota = 'C'
    if x >= 8.0:
        nota = 'B'
    if x >= 9.0:
        nota = 'A'
    if x <= 4.0:
        nota = 'F'
    return nota
notausuario = float(input('Digite a sua nota:\n').replace(',','.'))
print(f'Sua nota é {conceito(notausuario)}')