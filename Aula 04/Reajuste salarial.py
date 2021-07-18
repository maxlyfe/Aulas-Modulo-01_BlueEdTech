salario_inicial=float(input('Informe o seu salario atual \nR$'))
aumento = 0
percentual = 0

reajuste1 = 20
reajuste2 = 15
reajuste3 = 10
reajuste4 = 5

if salario_inicial <= 280:
  aumento = salario_inicial*(reajuste1/100)
  percentual = reajuste1
  print(f'Salario inicial R${salario_inicial}')
  print(f'{percentual}%')
  print(f'R${salario_inicial-aumento}')
  print(f'R${salario_inicial+aumento}')
elif salario_inicial < 700:
  aumento = salario_inicial*(reajuste2/100)
  percentual = reajuste2
  print(f'Salario inicial R${salario_inicial}')
  print(f'{percentual}%')
  print(f'R${salario_inicial-aumento}')
  print(f'R${salario_inicial+aumento}')
elif salario_inicial < 1500:
  aumento = salario_inicial*(reajuste3/100)
  percentual = reajuste3
  print(f'Salario inicial R${salario_inicial}')
  print(f'{percentual}%')
  print(f'R${salario_inicial-aumento}')
  print(f'R${salario_inicial+aumento}')
elif salario_inicial > 1500:
  aumento = salario_inicial*(reajuste4/100)
  percentual = reajuste4
  print(f'Salario inicial R${salario_inicial}')
  print(f'{percentual}%')
  print(f'R${salario_inicial-aumento}')
  print(f'R${salario_inicial+aumento}')
