from creation import vector
from creation import matrix
from newton import difdiv
from results import polynome
from results import mtx
from copy import deepcopy


#PROGRAMA PRINCIPAL
n = int(input('Digite a quantidade de pontos no Metodo Diferencas Divididas: '))
vetX = vector.criaX(n) #instanciacao de x como vetX
matFx = matrix.criaFx(n) #instanciacao da matriz fx como matFX
matAuxFx = deepcopy(matFx) #copia temporaria, total, da matFX para matAuxFx
matFx_final = difdiv.mtdDifDiv(vetX, matAuxFx) #instanciacao da matriz final como matFx_final
print('\n\nCRIADOS:\n') 
print(f'Vetor X = {vetX}\n')
print(f'Matriz Fx = {matFx}\n')
print(f'Matriz FINAL:\n')
#Disponibilizacao da Matriz Final em visual MATRICIAL (de forma usual)
mtx.showFinalMtx(vetX, matFx_final)
#Disponibilizacao do resultado final do polinomio literal & numerico
polynome.criarPolinomio(int(input('\nDigite o valor da ordem do Polinomio final: ')), vetX, matFx_final)
