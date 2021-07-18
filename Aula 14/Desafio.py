# DESAFIO -  Data com mês por extenso. 
# Construa uma função que receba uma data no formato DD/MM/AAAA 
# e devolva uma string no formato D de mesPorExtenso de AAAA. 
# Opcionalmente, valide a data e retorne NULL caso a data seja inválida. 
# Considere que Fevereiro tem 28 dias e que a cada 4 anos temos ano bisexto, 
# sendo que nesses casos Fevereiro terá 29 dias.

def nomemes (d,m,a):
    mes = ''
    if m == 1:
        mes = 'Enero'
    elif m == 2:
        mes = 'Febrero'
    elif m == 3:
        mes = 'Marzo'
    elif m == 4:
        mes = 'Abril'
    elif m == 5:
        mes = 'Mayo'
    elif m == 6:
        mes = 'Junio'
    elif m == 7:
        mes = 'Julio'
    elif m == 8:
        mes = 'Agosto'
    elif m == 9:
        mes = 'Septiembre'
    elif m == 10:
        mes = 'Octubre'
    elif m == 11:
        mes = 'Noviembre'
    elif m == 12:
        mes = 'Diciembre'
    return mes

dia = int(input('Digite o dia:\n'))
mes = int(input('Digite o mes:\n'))
ano = int(input('Digite o ano:\n'))
if dia == 29 and mes == 2:
    