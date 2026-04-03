'''O site está acessível?'''

import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print()
    print('O site Pudim não está disponível no momento.')
    print()
else:
    print()
    print('O site Pudim foi acessado com sucesso.')
    print()