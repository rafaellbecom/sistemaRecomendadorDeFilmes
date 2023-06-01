from baseDeDados import avaliacoes
from math import sqrt

#Distância Euclidiana
x = pow(3 - 3, 2)
y = pow(3.5 - 4, 2)
z = x + y
euclidiana = sqrt(z)
euclidianaP = (1/(1 + euclidiana)) * 100
print('{}% de similaridade'.format(euclidianaP))