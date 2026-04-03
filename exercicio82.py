'''Dividindo Valores em Várias Listas'''

lista = []
listapar = []
listaimpar = []

while True:
    n = int(input('Digite um número: '))
    lista.append(n)

    if n % 2 == 0:
        listapar.append(n)
    else:
        listaimpar.append(n)

    continuar = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Dados inválidos. Digite S para sim ou n para não: ')).upper().strip()[0]
    if continuar in 'N':
        break

print(f'Os valores da sua lista são: {lista}')
print(f'Os números pares são: {listapar}')
print(f'Os números ímpares são: {listaimpar}')
