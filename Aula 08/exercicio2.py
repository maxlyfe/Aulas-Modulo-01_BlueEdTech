#02 - Crie um programa que pergunte ao usuário um número inteiro e 
# faça a
# tabuada desse número.

lista = [1,2,3,4,5,6,7,8,9,10]

for i in range(len(lista)):
    num1 = int(input('Digite um numero:\n'))
    num2 = lista*num1

print(num2)
