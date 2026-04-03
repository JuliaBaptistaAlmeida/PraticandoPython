'''Valores Únicos'''
#a importância do sort

lista = []

while True:
    n = int(input('Digite um valor: '))
    if n in lista:
        print('Número duplicado, não ficará na lista.')
    else:
        lista.append(n)
    lista.sort()

    continuar = str(input('Deseja adicionar mais um? [S/N]: ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Dados inválidos. Digite S para sim e N para não: ')).upper().strip()[0]
    if continuar == 'N':
        break

print(f'Sua lista em ordem crescente ficou assim: {lista}')
