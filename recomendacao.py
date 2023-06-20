from baseDeDados import avaliacoesUsuario
from baseDeDadosInvertida import avaliacoesFilmes
from math import sqrt

#Euclidiana
def euclidiana(base, user1, user2) :
    si = {}
    ##Faz um loop for e armazena cada item da lista em uma variável item
    for item in base[user1]:
        ###Confere se os items da lista do user1 estão no user2
        if item in base[user2]: si[item] = 1
        
        if len(si) == 0: return 0
        
        soma = sum([pow(base[user1][item] - base[user2][item], 2)
                    for item in base[user1] if item in base[user2]])
        return 1/(1 + sqrt(soma))

#Similaridade
def getSimilares(base, user):
    similaridade = [(euclidiana(base, user, outro), outro) 
                    for outro in base if outro != user]
    similaridade.sort()
    similaridade.reverse()
    return similaridade[0:30]

#Recomendações
def getRecomendacoesUsuario(base, user):
    totais = {}
    somaSimilaridade = {}
    for outro in base:
        if outro == user: continue
        similaridade = euclidiana(base, user, outro)

        if similaridade <= 0: continue

        for item in base[outro]:
            if item not in base[user]:
                totais.setdefault(item, 0)
                totais[item] += base[outro][item] * similaridade
                somaSimilaridade.setdefault(item, 0)
                somaSimilaridade[item] += similaridade
    rankings = [(total / somaSimilaridade[item], item) for item, total in totais.items()]
    rankings.sort()
    rankings.reverse()
    return rankings[0:10]

#Carregar Movie Lens
def carregaMovieLens(path='C:/ml-100k'):
    filmes = {}
    for linha in open(path + '/u.item'):
        (id, titulo) = linha.split('|')[0:2]
        filmes[id] = titulo
    #print(filmes)
    base = {}
    for linha in open(path + '/u.data'):
        (usuario, idFilme, nota, tempo) = linha.split('\t')
        base.setdefault(usuario, {})
        base[usuario][filmes[idFilme]] = float(nota)
    return base

def calculaItensSimilares(base):
    result = {}
    for item in base:
        notas = getSimilares(base, item)
        result[item] = notas
    return result

def getRecomendacaoItens(baseUsuario, similaridadeItens, usuario):
    notasUsuario = baseUsuario[usuario]
    notas = {}
    totalSimilaridade = {}
    #Percorre todos os itens que o usuário deu uma nota
    for (item, nota) in notasUsuario.items():
        for (similaridade, item2) in similaridadeItens[item]:
            if item2 in notasUsuario: continue
            notas.setdefault(item2, 0)
            notas[item2] += similaridade * nota
            totalSimilaridade.setdefault(item2, 0)
            totalSimilaridade[item2] += similaridade
    rankings = [(score/totalSimilaridade[item], item) for item, score in notas.items()]
    rankings.sort()
    rankings.reverse()
    return rankings