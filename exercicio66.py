'''Somando Valores'''
#usando o break

soma = c = 0
while True:
    n = int (input('Digite um valor para ser somado ou 999 para parar: '))
    if n == 999:
        break
    soma += n
    c += 1
print (f'A soma dos {c} valores é igual a {soma}.')