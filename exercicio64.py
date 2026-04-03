'''Tratando Vários Valores'''

c = 0
soma = 0
n = 0
n = int (input ('Digite um valor ou digite 999 para encerrar: '))
while n != 999:
    c += 1
    soma += n 
    n = int (input ('Digite um valor ou digite 999 para encerrar: '))
print (f'Você digitou {c} valores e a soma deles é {soma}!')
