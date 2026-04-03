soma= 0
cont = 0
for c in range(1,7):
    n = int(input ('Digite um número inteiro: '))
    if n % 2 == 0:
        soma = n + soma
        cont = cont + 1
print (f'Você informou {cont} números pares, a soma deles resulta em {soma}')
