# Caixa eletrônico

# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.

# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;

# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

div100 = 100
div50 = 50
div10 = 10
div5 = 5
div1 = 1

resto100 = 100
resto50 = 50
resto10 = 10
resto5 = 5
resto1 = 1

nota_de_100 = 0
nota_de_100 = 0
nota_de_100 = 0
nota_de_100 = 0
nota_de_100 = 0

valor_saque = int(input('Qual valor você deseja sacar?\nR$'))

notas_int_100 = valor_saque//div100 #em unidades
notas_sobra_100 = valor_saque%div100 #em numero inteiro
notas_int_50 = notas_sobra_100//div50 #em unidades
notas_sobra_50 = notas_sobra_100%div50 #em numero inteiro
notas_int_10 = notas_sobra_50//div10 #em unidades
notas_sobra_10 = notas_sobra_50%div10 #em numero inteiro
notas_int_5 = notas_sobra_10//div5 #em unidades
notas_sobra_5 = notas_sobra_10%div5 #em numero inteiro
notas_int_1 = notas_sobra_5//div1 #em unidades
notas_sobra_1 = notas_sobra_5%div1 #em numero inteiro


if valor_saque >= 10 or valor_saque <= 600:
  print(f'O valor de R${valor_saque} vai te entregar:\n{notas_int_100} notas de R$100,00\n{notas_int_50} notas de R$50,00\n{notas_int_10} notas de R$10,00\n{notas_int_5} notas de R$5,00\n{notas_int_1} notas de R$1,00')
