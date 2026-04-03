'''Testando help'''

def somar(a, b, c):
    """ => faz a soma de três valores e mostra o resultado na tela.
    - Para a: O primeiro valor.
    - Para b: O segundo valor.
    - Para c: O terceiro valor.
    => Funcao criada por Xu
    """ #criou uma docstring para sair no help()
    s = a + b + c
    print(f'A soma resulta em {s}')

somar(3, 2, 5)
help(somar)
