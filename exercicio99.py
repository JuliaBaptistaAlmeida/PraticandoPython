'''Função para Descobrir o Maior'''

def maior(* n):
    c = maior = 0
    print('Analisando os valores recebidos: ', end='')
    for valor in n:
        print(f'{valor}', end=' ')

        if c == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        c += 1

    print(f'\nForam informados {c} valores.')
    print(f'O maior valor foi {maior}.')

#Programa Principal
lista = []

while True:
    valores = int(input('Informe um valor para adicionar a lista: '))
    lista.append(valores)
    
    continuar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Dados inválidos. Digite S para sim ou N para não: ')).upper().strip()[0]
    if continuar == 'N':
        break

print('~~' * 20)
maior(* lista)
print('~~' * 20)
