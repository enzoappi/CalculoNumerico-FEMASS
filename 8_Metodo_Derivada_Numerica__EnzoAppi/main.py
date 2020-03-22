from derivative import simple
from derivative import three_points
from derivative import five_points

#Programa principal
print(f'\nA derivada simples da funcao eh: {simple.derivada_simples(2)}\n')
print(f'\nA derivada da funcao, por 3 pontos eh: {three_points.derivada_TresPts(2)}\n')
print(f'\nA derivada da funcao, por 5 pontos eh: {five_points.derivada_CincoPts(2)}')