'''Maior e Menor'''

maior = 0
menor = 0
for pessoa in range(1, 6):
    peso = float(input (f'Qual o peso da {pessoa}ª pessoa? '))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print (f'O menor peso lido foi {menor}Kg, e o maior foi {maior}Kg')