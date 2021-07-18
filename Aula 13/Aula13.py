# Faça um programa que tenha uma função chamada área(), 
# que receba as dimensões de um terreno retangular (largura e comprimento) 
# e mostre a área do terreno:
def area(comprimento,largura):
    r=comprimento*largura
    print(f'A area é de {r:.2f}')

c=float(input('Digite o comprimento:\n'))
l=float(input('Digite a largura:\n'))
area(c,l)
