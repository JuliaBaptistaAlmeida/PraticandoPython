'''Formatando Moedas parte 2'''
#mais facil fazer como no 107...

from pacote import modulos

preço = float(input('Digite o preço: R$ '))

print()
print(f'A metade de {modulos.moeda(preço)} é {modulos.moeda(modulos.metade(preço))}.')
print(f'O dobro de {modulos.moeda(preço)} é {modulos.moeda(modulos.dobro(preço))}.')
print(f'Aumentando 10%, temos R$ {modulos.moeda(modulos.aumentar(preço, 10))}.')
print(f'Com desconto de 10%, temos R$ {modulos.moeda(modulos.diminuir(preço, 10))}.')
print()