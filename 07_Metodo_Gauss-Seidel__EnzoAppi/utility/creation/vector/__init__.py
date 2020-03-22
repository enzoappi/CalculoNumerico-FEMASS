#Criando o Vetor X (CHUTE) ou Vetor B (valores do sistema)
def CriarVetor(a, b):
  vetor = list()
  print('\n')
  for i in range(0, a):
    vetor.append(float(input(f'Digite um numero para o {i + 1}º elemento do vetor_{b}: ')))
  print(f'\n\nVetor_{b} = {vetor}')
  return(vetor)
