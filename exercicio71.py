'''Caixa Eletrônico'''

print('=' * 20)
print(f'{"BANCO COM X":^20}')
print('=' * 20)

valor = int(input('Que valor você deseja sacar? '))
total = valor
ced = 100
totcedulas = 0

while True:
    if total >= ced:
        total -= ced
        totcedulas += 1
    else:
        if totcedulas > 0:
            if ced == 1:
                print(f'Total de {totcedulas} moeda(s) de R$ {ced}.')
            else:
                print(f'Total de {totcedulas} cédula(s) de R$ {ced:.2f}.')
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 1
        totcedulas = 0
        if total == 0:
            break

print('=' * 20)
print('Volte sempre ao Banco Com X!')
