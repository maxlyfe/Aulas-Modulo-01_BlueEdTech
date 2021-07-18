# 9.Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos
# elementos do vetor.

lista=[]

vezes =0
while vezes != 10:
    num = int(input('Digite um valor:\n'))
    num2 = num*num
    lista.append(num2)
    vezes +=1

resultado=sum(lista)
print(resultado)