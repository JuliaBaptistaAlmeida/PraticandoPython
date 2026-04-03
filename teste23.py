'''Dicionários'''

pessoas = {'Nome': 'Xu', 'Idade': 22, 'Sexo': 'F'}
pessoas['Nome'] = 'Julia' #substitui
pessoas['Peso'] = 60 #adiciona, substituindo o append

print(pessoas['Idade'])
print(f'A {pessoas['Nome']} tem {pessoas['Idade']} anos de idade.')
print(pessoas.values()) #mostra os dados da pessoa
print(pessoas.keys()) #mostra o que foi pedido(nome, idade, sexo)
print(pessoas.items()) #mostra tudo
print(pessoas['Peso'])
print()

for k in pessoas.keys():
    print(k)

print()

for v in pessoas.values():
    print(v)

print()

for k, v in pessoas.items(): #substitui o enumerate
    print(f'{k} = {v}')
    