# 1.	Faça um programa, com uma função que necessite de três argumentos, 
# e que forneça a soma desses três argumentos.

def soma(x,y,z):
    somar = x+y+z
    return somar

num1 = float(input('Digite um numero:\n'))
num2 = float(input('Digite outro numero:\n'))
num3 = float(input('Digite outro numero:\n'))
resultado = soma(num1,num2,num3)
print(f'A soma dos numeros {num1}, {num2} e {num3} é de {resultado}')