'''Lista de Preços'''

lista = ('esmalte', 4.75,
        'esfoliante', 9.99,
        'shampoo', 18,
        'condicionador', 18,
        'acetona', 6,
        'body splash', 23.99,
        'creme corporal', 19.90,
        'algodão', 12,)

print('=' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('=' * 40)

for pos in range(0, len(lista)):
    if pos % 2 == 0: #par porque os nomes estao nas posiçoes pares e o valor nas ímpares
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'R${lista[pos]:>6.2f}')
print('=' * 40)
