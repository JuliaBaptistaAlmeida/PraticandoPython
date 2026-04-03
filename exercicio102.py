'''Função para Fatorial'''
#usando show pela primeira vez

def fatorial(n, show=False):
    """Calcula o fatorial de um número:
    - Para n: O número que vai ser mostrado o fatorial.
    - Para show: True para mostrar a conta e False para mostrar só o resutado.
    - Return: Retorna o fatorial de n."""

    f = 1

    for c in range(n, 0, -1):
        if show:
            print(c, end=' ')
            if c > 1:
                print('X', end=' ')
            else:
                print('=', end=' ')  
        f *= c
    return f

#Programa Principal
num = int(input('Digite um número para ver seu fatorial: '))
print(fatorial(num, show=False))
print()
conta = str(input('Deseja exibir o cálculo? [S/N] ')).upper().strip()[0]
while conta not in 'SN':
    conta = str(input('Dados inválidos. Digite S para sim ou N para não: ')).upper().strip()[0]
if conta == 'S':
    print(fatorial(num, show=True))
    print()

print('Fim do Programa!')
