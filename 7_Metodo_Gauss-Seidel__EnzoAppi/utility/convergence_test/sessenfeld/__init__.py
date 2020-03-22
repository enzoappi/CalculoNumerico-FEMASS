#Criando o teste de convergencia 2 (Criterio de Sessenfeld):
def convergencia_2(matriz, num):
  print('\n\nCriterio de Sessenfeld:')
  beta = list()
  for i in range(0, num):
    beta.append(1)
  for l in range(0, num):
    soma = 0;
    for c in range(0, dimensao):
      if c != l:
        soma = soma + (math.fabs(matriz[l][c]) * beta[c])
    beta[l] = (soma / math.fabs(matriz[l][l]))
  print(f'\nBeta = {beta}')
  print(f'O maior valor em Beta eh: {max(beta)}')
  return(max(beta))
