'''Erros e Exceções'''

try:
    a = int(input('Digite o numerador: '))
    b = int(input('Digite o denominador: '))
    resposta = a / b
except Exception as erro: #Exception vai fazer mostrar qual a exceção
    print(f'Erro encontrado: {erro.__class__}')  #esclohi o que ia mostrar (classe da exceção)
else:
    print(f'O resultado é: {resposta}.')
finally:
    print('Volte Sempre!')
