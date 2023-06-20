from baseDeDados import avaliacoesUsuario
from baseDeDadosInvertida import avaliacoesFilmes
from recomendacao import *

'''
##Cálculo da Distância Euclidiana
#Função pow() eleva ao quadrado
#x = pow(3 - 1.5, 2)
#y = pow(3.5 - 5, 2)
#z = x + y
#euclidiana = sqrt(z)
#euclidianaP = (1/(1 + euclidiana)) * 100
#print('{}% de similaridade'.format(euclidianaP))
#print('----------')

##Testando Função Euclidiana
print('A similaridade é de: {}'.format(euclidiana('Ana', 'Pedro')))
print('----------')

##Cálculo de Similaridade com todos
print('A similaridade é de: {}'.format(getSimilares('Marcos')))
print('----------')

##Testando Função de Recomendação
print('A similaridade é de: {}'.format(getRecomendacoes('Janaina')))
print('----------')

##Filmes Similares
print('A similaridade é de: {}'.format(getRecomendacoes(avaliacoesFilmes, 'Star Wars')))
print('----------')

##Movie Lens
base = carregaMovieLens()
print(getRecomendacoes(base, '212'))

##Como fazer Recomendação - Itens
itensSimilares = calculaItensSimilares(avaliacoesFilmes)
print(itensSimilares)
'''
##Recomendação por Usuários x Recomendação por Itens
#print(getRecomendacoesUsuario(avaliacoesUsuario, 'Leonardo'))

#itensSimilares = calculaItensSimilares(avaliacoesFilmes)
#print(getRecomendacaoItens(avaliacoesUsuario, itensSimilares, 'Leonardo'))

base = carregaMovieLens()
print(getRecomendacoesUsuario(base, '6'))