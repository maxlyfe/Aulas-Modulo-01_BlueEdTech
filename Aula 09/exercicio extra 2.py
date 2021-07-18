# 10.Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos,
# cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

lista=[]
lista2=[]
vezes =0
while vezes != 10:
    num = int(input('Digite um valor:\n'))
    lista.append(num)
    vezes +=1
vezes=0
while vezes != 10:
    num = int(input('Digite um valor:\n'))
    lista2.append(num)
    vezes +=1
lista3=[lista+lista2]

print(lista3)
