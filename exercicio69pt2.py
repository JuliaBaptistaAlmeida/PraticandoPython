'''Análise de Grupo'''
#aprendendo como o guanabara fez
#no anterior eu entendi o enunciado errado

maiores = homens = mulheres20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]
    while sexo not in 'MF':
        sexo = str(input('Dados inválidos. Digite M para masculino ou F para feminino: ')).upper().strip()[0]
    if idade >= 18:
        maiores += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres20 += 1

    resposta = str(input('Deseja adicionar mais um? [S/N]: ')).upper().strip()[0]
    while resposta not in 'SN':
        resposta = str(input('Dados inválidos. Digite S para sim e N para não: ')).upper().strip()[0]
    if resposta == 'N':
        break

print(f'Total de maiores de idade: {maiores}')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'E temos {mulheres20} mulheres com menos de 20 anos.')
