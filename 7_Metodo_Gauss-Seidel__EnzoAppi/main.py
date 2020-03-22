from utility.convergence_test import linecolumndominant
from utility.convergence_test import sessenfeld
from utility.creation import matrix
from utility.creation import vector
from utility import gauss_seidel

#Programa Principal
#Solicitacao da dimensao da Matriz A e dos vetores b e X:
dimensao = int(input('Digite a dimensao: '))
#Chamando a funcao para criar a Matriz A:
matriz_A = matrix.CriarMatriz(dimensao, 'A')
#Chamando a funcao para criar o Vetor B:
vetor_b = vector.CriarVetor(dimensao, 'b')
#Chamando a funcao para criar o Vetor X (CHUTE):
vetor_X = vector.CriarVetor(dimensao, 'X')
#Chamando a funcao para testar a convergencia 1, do Sistema:
Diag_Dom = linecolumndominant.convergencia_1(matriz_A, dimensao)
#Teste logico para o prosseguimento, ou nao, da utilizacao do metodo Gauss-Seidel:
if Diag_Dom == 1:
  #Chamando a funcao para testar a convergencia 2, do Sistema:
  Sessenfeld = sessenfeld.convergencia_2(matriz_A, dimensao)
  #Teste logico para o prosseguimento, ou nao, da utilizacao do metodo Gauss-Seidel:
  if Sessenfeld < 1:
    print('\nComo Beta < 1...\n   Prosseguiremos com o Metodo Gauss-Siedel...')
  #Chamando a funcao para iniciar o METODO GAUSS-SEIDEL:
    gauss_seidel.Gauss_Seidel(matriz_A, vetor_b, vetor_X, dimensao)
