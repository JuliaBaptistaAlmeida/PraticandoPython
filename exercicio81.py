'''Extraindo Dados de uma Lista'''

c = 0
lista = []

while True:
    n = int(input('Digite um número inteiro: '))
    lista.append(n)
    lista.sort(reverse = True)
    c += 1

    continuar = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Dados inválidos. Digite S para sim ou N para não: ')).upper().strip()[0]
    if continuar == 'N':
            break
    
print(f'Sua lista possui {c} valores, sendo eles: ', end='')
print(f'{lista}, em ordem decrescente.')
if 5 in lista:
    print('O número 5 está presente na lista.')
else:
     print('O número 5 não está presente na lista.')
     