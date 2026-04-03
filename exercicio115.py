from ex115.interface import *
from ex115.lib import *

arq = 'cursoemvideo.txt'

if not arquivoexiste(arq):
    criararquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        leiaarquivo(arq)
        
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        if nome == '':
            nome = 'desconhecido'
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)

    elif resposta == 3:
        cabeçalho('Saindo do sistema... Até logo!')
        break

    else:
        print('\033[31mERRO! Digite uma opção válida.\033[m')
