'''Números Primos'''

# Resetando as cores antes do input
print('\033[m', end='')  #reseta a cor para o padrão
total = 0
n = int (input('Digite um número: '))
for c in range(1, n + 1):
    if n % c == 0:
        print ('\033[32m', end = '')
        total = total + 1
    else:
        print ('\033[31m', end = '')
    print (f'{c}', end = ' ')
print('\033[m', end='')
print (f'O número {n} foi divisível {total} vezes...')
if total == 2:
    print (f'Portanto, o número {n} é PRIMO!')
else:
    print (f'Portanto, o número {n} NÃO é primo!')
