# Faça um script que o usuário escolha um número de início, um número de fim, e um número de
# passo. O programa deve printar todos os números do intervalo entre início e fim, "pulando" de
# acordo com o intervalo passado

inicio = int(input('Digite um número de inicio:\n'))
final = int(input('Digite o número final:\n'))
intervalo = int(input('Digite qual vai ser o intervalo:\n'))
lista = [inicio,final, intervalo]
for i in range(inicio,final, intervalo):
  print()
  print(i)
