'''Formatando Moedas, parte 6'''
#agora ele aceita entrada str, vazia e com ,

from pacote import dados
from pacote import moeda

preço = dados.leiadinheiro('Digite o preço: R$ ')
moeda.resumo(preço)
