'''Matriz em Python parte 2'''

matriz = [[0, 0 , 0], [0, 0, 0], [0, 0, 0]]
somapar = somacoluna = maior = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha] [coluna] = int(input(f'Digite um valor para {linha} e {coluna}: '))

print('=-' * 12)

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            somapar += matriz[linha][coluna]
    print()

print(f'A soma dos números pares é igual a {somapar}.')

for linha in range(0, 3):
    somacoluna += matriz[linha][2]

print(f'A soma da terceira coluna é igual a {somacoluna}.')

for coluna in range(0, 3):
    if coluna == 0 or matriz[1][coluna] > maior:
        maior = matriz[1][coluna]

print(f'O maior valor da segunda linha é {maior}.')
