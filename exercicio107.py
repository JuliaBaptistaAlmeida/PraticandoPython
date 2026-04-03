'''Formatando Moedas parte 1'''
#criando pacote e modulos

from pacote import modulos

preço = float(input('Digite o preço: R$ '))

print()
print(f'A metade de R$ {preço:.2f} é {modulos.metade(preço)}.')
print(f'O dobro de R$ {preço:.2f} é {modulos.dobro(preço)}.')
print(f'Aumentando 10%, temos R$ {modulos.aumentar(preço, 10)}.')
print(f'Com desconto de 10%, temos R$ {modulos.diminuir(preço, 10)}.')
print()
