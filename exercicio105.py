'''Analisando e Gerando Dicionários'''

def notas(* n, situacao=False):

    """=> Funcao para analisar notas e situacoes de varios alunos.
    - para n: uma ou mais notas.
    - para situacao: valor opcional, se vai ou nao indicar a situacao da turma.
    - return: retorna dicionario com as informacoes dos alunos. """

    r = {}
    r['Total de notas'] = len(n)
    r['Maior nota'] = max(n)
    r['Menor nota'] = min(n)
    r['Média da turma'] = sum(n) / len(n) #usando sum pela primeira vez

    if situacao:
        if r['Média da turma'] >= 7:
            r['Situação'] = 'BOA'
        elif r['Média da turma'] >= 5:
            r['Situação'] = 'RAZOÁVEL'
        else:
            r['Situação'] = 'RUIM'
    return r

#Programa Principal
lista = []

while True:
    aluno = float(input('Digite a nota do aluno: '))
    lista.append(aluno)
    continuar = str(input('Deseja continuar? [S/N]')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Dados inválidos. Digite S para sim ou N para não: ')).upper().strip()[0]
    if continuar == 'N':
        break

print(notas(*lista, situacao=True))
print()
print('~~' * 40)
print()
help(notas)
