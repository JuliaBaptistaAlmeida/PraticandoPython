'''Função que Calcula Área'''

def area(largura, comprimento):
    a = largura * comprimento
    print(f'A área do terreno {largura} X {comprimento} é igual a {a}m².')

#Programa Principal
l = float(input('Digite a largura do terreno: '))
c = float(input('Digite o comprimento do terreno: '))
print()
print('=-' * 20)
print('DIMENSÕES DO TERRENO')
print()
area(l, c)
print('=-' * 20)
