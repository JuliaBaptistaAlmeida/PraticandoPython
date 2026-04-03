'''Aumento Salarial'''

salario = float(input ('Qual o valor do salário atual? '))
if salario <= 1250:
    aumento = salario + (salario * 15 / 100)
    print (f'Com o aumento de 15%, o salário passará a ser R$ {aumento:.2f}')
else:
    aumento = salario + (salario *10 / 100)
    print (f'Com o aumento de 10%, o salário passará a ser R$ {aumento:.2f}')
