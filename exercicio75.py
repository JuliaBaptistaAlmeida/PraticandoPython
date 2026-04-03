'''Análise de Dados em uma Tupla'''

n = (int(input('Digite um número: ')), 
    int(input('Digite um número: ')),
    int(input('Digite um número: ')),
    int(input('Digite um número: ')))

print(f'Você digitou os valores {n}.')

print(f'O número 9 apareceu {n.count(9)} vezes.')
if 3 in n:
    print(f'O valor número 3 aparece pela primeira vez na posição {n.index(3)+1}.')
else:
    print('O número 3 não foi digitado.')

par = False 
for num in n:
    if num % 2 == 0:
        print('Os números pares foram:', end=' ')
        print(num, end=' ')
        par = True
if not par:
    print('Não há números pares.')

print('\nFIM!')
