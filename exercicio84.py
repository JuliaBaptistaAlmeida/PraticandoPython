'''Lista Composta e Análise de Dados'''

inicial = []
final = []
maior = menor = 0

while True:
    inicial.append(str(input('Nome: ')))
    inicial.append(float(input('Peso: ')))
    
    if len(final) == 0:
        maior = menor = inicial[1]
    else:
        if inicial[1] > maior:
            maior = inicial[1]
        if inicial[1] < menor:
            menor = inicial[1]

    final.append(inicial[:])
    inicial.clear()

    continuar = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Dados inválidos. Digite S para sim ou N para não: ')).upper().strip()[0]
    if continuar == 'N':
        break

print(f'Os dados foram {final}.')
print(f'Foram cadastradas {len(final)} pessoas.')
print(f'O maior peso foi {maior}Kg, de ', end='')
for p in final:
    if p[1] == maior:
        print(f'{p[0]}')
print(f'O menor peso foi {menor}Kg, de ', end='')
for p in final:
    if p[1] == menor:
        print(f'{p[0]}')
