'''Dicionários'''

estado = {}
brasil = []

for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy()) #copy substitui o [:]

print(brasil)
