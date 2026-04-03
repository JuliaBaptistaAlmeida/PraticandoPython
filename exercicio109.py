'''Formatando Moedas, parte 3'''

from pacote import modulos

preço = float(input('Digite o preço: R$ '))

print()
print(f'A metade de {modulos.moeda(preço)} é {modulos.metade(preço, True)}.')
print(f'O dobro de {modulos.moeda(preço)} é {modulos.dobro(preço, True)}.')
print(f'Aumentando 10%, temos R$ {modulos.aumentar(preço, 10, True)}.')
print(f'Com desconto de 10%, temos R$ {modulos.diminuir(preço, 10, True)}.')
print()