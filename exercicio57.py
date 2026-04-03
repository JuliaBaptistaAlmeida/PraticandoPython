'''Conferindo Dados'''

sexo = str (input('Informe seu sexo [M ou F]:')) .strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str (input('Dados inválidos, informe seu sexo M ou F:')) .strip().upper()[0]
print (f'Sexo {sexo} registrado com sucesso.')