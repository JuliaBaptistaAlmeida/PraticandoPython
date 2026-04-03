'''Calculando o Fatorial'''
#sem usar o math

n = int (input('Digite um número: '))
c = n
fatorial = 1 #porque tem que parar no x1
print (f'Calculando {n}!: ', end='')
while c > 0:
    print (f'{c}', end= ' ')
    print ('X' if c > 1 else ' = ', end= ' ')
    fatorial *= c
    c -= 1
print (f'{fatorial}')
