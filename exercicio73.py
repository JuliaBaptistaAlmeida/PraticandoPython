'''Tuplas com Times de Futebol'''

print('=-' * 15)
print(f'{"BRASILEIRÃO":^30}')
print('=-' * 15)

times = ('Botafogo', 'Palmeiras', 'Flamengo',
        'Fortaleza', 'Internacional', 'São Paulo',
        'Corinthians', 'Bahia', 'Cruzeoro' 'Vasco da Gama'
        'EC Vitória', 'Atlético-MG', 'Fluminense', 'Grêmio'
        'Juventude', 'Bragantino', 'Atlético-PR',
        'Criciúma', 'Atlético-GO', 'Cuiabá')

print(f'Os 5 primeiros colocados são: {times[:5]}')
print('=-' * 40)
print(f'Os 5 últimos colocados são: {times[-5:]}')
print('=-' * 40)
print(f'Lista em ordem alfabética: {sorted(times)}')
print('=-' * 40)
print(f'O Corinthians está na posição número {times.index('Corinthians')}')
print('=-' * 40)
