from recomendacao import *

base = carregaMovieLens()
print(getRecomendacoesUsuario(base, '212'))