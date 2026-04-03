'''Ficha do Jogador'''

def ficha(nome, gols):
    if nome == '':
        nome = '<desconhecido>'
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    return f'O jogador {nome} fez {gols} gols.'


nome = str(input('Nome do jogador: '))
gols = str(input('Número de gols: '))

print(ficha(nome, gols))
