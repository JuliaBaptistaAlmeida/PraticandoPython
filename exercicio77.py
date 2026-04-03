'''Contando Vogais'''

palavras = ('pitico', 'doralice', 'nina', 'xulia', 'faculdade',
        'escrever', 'digitar', 'sonhar', 'pedra', 'curso')

for p in palavras:
    print(f'\nNa palavra {p} temos ', end='')
    for vogal in p:
        if vogal.lower() in 'aeiou':
            print(vogal, end=' ')
