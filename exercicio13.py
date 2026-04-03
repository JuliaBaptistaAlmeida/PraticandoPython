'''Aumento Salarial'''

atual = float(input('Qual é o salário atual? R$ '))
aumento = (atual * 15) / 100
novo = atual + aumento
print(f'Recebendo um aumento de 15%, o sálario novo será de R$ {novo:.2f}.')
