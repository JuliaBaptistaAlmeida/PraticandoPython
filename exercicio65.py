'''Analisando Valores'''

continuar = 'S'
c = soma = media = maior = menor = 0
while continuar in 'Ss':
    n = int (input('Digite um valor inteiro: '))
    c += 1
    soma += n
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    continuar = str (input('Quer continuar? [S/N] ')).upper().strip()[0]
media = soma / c
print (f'Você digitou {c} valores, a soma deles é {soma},', end= '')
print (f'a média é {media:.2f}, o maior valor foi {maior} e o menor foi {menor}.')
