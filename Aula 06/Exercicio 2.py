#Desenvolva um código que pergunte um número n para o usuário e exiba todos seus divisores

soma = 0

num = int(input('Digite um número:\n')) # quantidade de numeros que serão somados

for i in range(num):
    soma = soma + int(input('Qual é o numero da vez?:\n'))
print(f'A soma é {soma}')
print('oi')
