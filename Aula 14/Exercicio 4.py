# 4.	Faça um programa que calcule o salário de um colaborador na empresa XYZ. 
# O salário é pago conforme a quantidade de horas trabalhadas. 
# Quando um funcionário trabalha mais de 40 horas ele recebe um adicional de 1.5 nas horas extras trabalhadas.
def salario(x,y):
    salariobase = x*y 
    salarioextra = 0
    if y > 40:
        salarioextra = (y-40)*1.5

    return salarioextra + salariobase
   
valorxhora = 10
colaborador = float(input('Quantas horas você trabalhou?\n').replace(',','.'))
print(f'Seu salario com {colaborador}horas trabalhadas é de R${salario(valorxhora,colaborador)}')