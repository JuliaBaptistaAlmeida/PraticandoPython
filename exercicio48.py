'''Somando ímpares múltiplos de três'''

soma = 0
cont = 0
for tres in range(1, 501, 2):
    if tres % 3 == 0:
        soma = soma + tres
        cont = cont + 1
print (f'A soma de {cont} os valores é: {soma}')
