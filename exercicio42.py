'''Analisando Triângulos'''

r1 = float(input ('Segmento 1: '))
r2 = float(input ('Segmento 2: '))
r3 = float(input ('Segmento 3: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 +r2:
    print ('Os segmentos acima PODEM formar um triângulo!', end = ' ')
    if r1 == r2 == r3:
        print ('EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print ('ESCALENO')
    else:
        print ('ISÓSCELES')
else:
    print ('Os segmentos acima NÃO PODEM formar um triângulo.') 
