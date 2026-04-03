'''Lista com Pares e Ímpares'''

lista = []
pares = []
impares = []
c = 1

for n in range(0,7):
    valor = (int(input(f'Digite o valor {c}: ')))
    lista.append(valor)
    c += 1
    if valor % 2 == 0:
        pares.append(valor)
    else:
        impares.append(valor)

lista.sort()
pares.sort()
impares.sort()

print(f'Os números cadastrados foram: {lista}')
print(f'Os números pares são: {pares}')
print(f'Os números ímpares são: {impares}')
