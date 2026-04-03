'''Análise de Grupo'''

homens = mulheres = maiores = 0

while True:
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()[0]

    while sexo not in 'MF':
        sexo = str(input('Dados inválidos. Digite F para feminino ou M para masculino: '))
    
    if idade >= 18:
        maiores += 1
    
    if sexo == 'F':
        mulheres += 1
    elif sexo == 'M':
        homens += 1
       
    continuar = str(input('Deseja adicionar mais um? [S/N]: ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Dados inválidos. Digite S para sim e N para não: ')).upper().strip()[0]
    
    if continuar == 'N':
        break

total = mulheres + homens
print(f'Nesse formulário há {total} pessoas. {mulheres} mulheres {homens} homens, ', end='')
print(f'sendo {maiores} deles maiores de idade.')
