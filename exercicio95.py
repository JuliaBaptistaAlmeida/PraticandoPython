'''Jogador de Futebol parte 2'''

dados = {}
lista = []
time = []

while True:
    dados.clear()
    c = 1

    dados['Nome'] = str(input('Nome do Jogador: '))
    dados['Partidas'] = int(input(f'Quantas partidas {dados['Nome']} jogou? '))

    lista.clear()

    for j in range (dados['Partidas']):
        lista.append(int(input(f'Quantos gols {dados['Nome']} fez na partida {c}? ')))
        c += 1

    dados['Gols Partida'] = lista[:]
    dados['Total de Gols'] = sum(lista)

    time.append(dados.copy())

    continuar = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Dados inváidos. Digit S para sim ou N para não: ')).upper().strip()[0]
    if continuar == 'N':
        break

print('==' * 40)

print('nº', end='')
for i in dados.keys():
    print(f'{i:>17}', end='')
print()

for k, v in enumerate(time):
    print(f'{k}', end='')
    for dado in v.values():
        print(f'{str(dado):>17}', end='') #vai converter qualquer valor para string ''
    print()

print('==' * 40)

while True:
    jogador = int(input('Mostrar os dados de qual jogador? (999 para parar): '))
    if jogador == 999:
        break
    if jogador >= len(time):
        print('Dados inválidos. Jogador não encontrado.')
    else:
        print(f'DADOS DO JOGADOR:')
        for n, gols in enumerate(time[jogador]['Gols Partida']):
            print(f'No jogo {n+1} fez {gols} gols.')
    
print('FIM DO PROGRAMA')
