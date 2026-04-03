'''Validando Expressões Matemáticas'''

exp = str(input('Digite uma expressão matemática: '))
pilha = []
for simbolo in exp:
    if simbolo == '(':
        pilha.append('(')
    elif simbolo == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
        
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está inválida!')
