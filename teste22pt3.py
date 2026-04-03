'''Listas Dentro de Listas'''

galera = []
dado = []

for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear() #esvazia a lista para nova repetição

print(galera)
