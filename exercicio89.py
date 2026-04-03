'''Boletim com Listas Compostas'''

alunos = int(input('Quantos alunos serão registrados? '))
c = 1
lista = []

for a in range(0, alunos):
    aluno = str(input(f'Aluno {c}: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    nota3 = float(input('Nota 3: '))
    media = (nota1 + nota2 + nota3) / 3
    lista.append([aluno, [nota1, nota2, nota3], media])
    c += 1

print('=-' * 15)
print(f'{"BOLETIM ESCOLAR":^25}')
print('=-' * 15)

print(f'{'Nº':<4}{'NOME':<10}{'MÉDIA':>8}')
for p, n in enumerate(lista):
    print(f'{p:<4}{n[0]:<10}{n[2]:>8.1f}')

while True:
    print('=-' * 15)
    opçao = int(input('Qual o número do aluno que você deseja ver as notas? (999 para interromper): '))
    if opçao <= len(lista) -1:
        print(f'Notas de {lista[opçao][0]} são {lista[opçao][1]}.')
    if opçao == 999:
        print('FINALIZANDO...')
        break
print('FIM DO PROGRAMA!')
