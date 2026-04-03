'''Média'''

nota1 = float (input ('Digite a primeira nota: '))
nota2 = float (input ('Digite a segunda nota: '))
nota3 = float (input ('Digite a terceira nota: '))
media = (nota1 + nota2 + nota3) / 3
if media < 6 and media > 3:
    print (f'Sua média é {media:.2f}, você está de RECUPERÇÃO!')
elif media < 4:
    print (f'Sua média é {media:.2f}, você foi REPROVADO(A)!')
elif media >= 6:
    print (f'Sua média é {media::.2f}, você foi APROVADO(A)!')
else:
    print ('Digite um valor válido!')
