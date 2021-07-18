# 2.	 Faça um programa, com uma função que necessite de um argumento. 
# A função retorna o valor de caractere ‘P’, se seu argumento for positivo, ‘N’, 
# se seu argumento for negativo e ‘0’ se for 0.

def funcao(r):
    if r > 0:
        return 'P'
    elif r < 0:
        return 'N'
    elif r == 0:
        return '0'

usuario = float(input('Digite um numero:\n'))
print(funcao(usuario))