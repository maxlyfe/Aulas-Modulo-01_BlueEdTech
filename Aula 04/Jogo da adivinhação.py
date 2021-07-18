import random 

num_usuario = int(input('Adivinhe qual é o número no qual estou pensado, digite um numero de 0 a 10:\n'))
num_us = num_usuario
num_computador = random.randint(0,10)

numfinal = num_computador

if num_usuario == num_computador:
  print('Parabens você acertou!')

elif num_usuario != num_computador:
  print('Você errou.')
  print(f'O numero era {numfinal}')
