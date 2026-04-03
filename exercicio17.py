'''Catetos e Hipotenusa'''
# Sem importação de módulos

co = float(input ('Digite o comprimento do cateto oposto: '))
ca = float(input ('Digite o comprimento do cateto adjacente: ')) 
hi = (co**2 + ca**2) **(1/2)
print (f'A hipotenusa do triângulo retângulo mede {hi:.2f}.')
