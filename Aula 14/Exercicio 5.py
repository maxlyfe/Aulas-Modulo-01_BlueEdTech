# 5.	Faça um programa que calcule através de uma função o IMC de uma pessoa que tenha 1,68 e pese 75kg.
def imc (x,y):
    imcfinal = x/(y**2)
    return imcfinal
peso = float(input('Digite o seu peso em Kg:\n').upper().replace('K','').replace('G','')) #75
altura = float(input('Digite a sua altura em m:\n').upper().replace(',','.').replace('M','')) #1.68
print(f'Seu IMC é de {imc(peso,altura):.2f}')