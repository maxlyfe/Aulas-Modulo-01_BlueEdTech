# 7.	Escreva uma função que recebe dois parâmetros e imprime o menor dos dois. 
# Se eles forem iguais, imprima que eles são iguais.
def batata (x,y):
    if x>y:
        print(y)
    elif y>x:
        print(x)
    elif x==y:
        print('Os valores são iguais.')
num1 = float(input('Digite o primeiro número:\n').replace(',','.'))
num2 = float(input('Digite o segundo número:\n').replace(',','.'))
print()
batata(num1,num2)