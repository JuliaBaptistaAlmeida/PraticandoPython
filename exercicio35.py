'''Analisando um Triângulo'''

print ('-=-' * 16)
print ('Analisador de Triângulos...')
print ('-=-' * 16)
r1 = float(input ('Segmento 1: '))
r2 = float(input ('Segmento 2: '))
r3 = float(input ('Segmento 3: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 +r2:
    print ('Os segmentos acima PODEM formar um triângulo!')
else:
    print ('Os segmentos acima NÃO PODEM formar um triângulo.') 
