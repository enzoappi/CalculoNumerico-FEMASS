from numpy import linalg
from numpy import array
from numpy import s_
from numpy import delete
from copy import deepcopy

#Funcao de calculo da Matriz Inversa
def criaMatrizInversa(ordem, matriz):
    mat_aux = array(matriz) #Criando uma matriz auxiliar exatamente igual a matriz de entrada
    mat_aux = delete(delete(mat_aux, s_[ordem:], 0), s_[ordem:], 1) #cortando as linhas e colunas que não são necessarias ao sistema
    matxMinor = list()
    matxCoef_aux = list()
    matxCoef = list()
    for l in range(0, ordem):
        for c in range(0, ordem):
            matxMinor = delete(delete(mat_aux, l, 0), c, 1)
            cofator = pow(-1, (l + c)) * linalg.det(matxMinor)
            matxCoef_aux.append(cofator)
        matxCoef.append(matxCoef_aux[:])
        matxCoef_aux.clear()
    detMatriz = linalg.det(mat_aux)
    matxInv = deepcopy(matxCoef)
    for c in range(0, ordem):
        for l in range(0, ordem):
            matxInv[l][c] = matxCoef[c][l] / detMatriz
    return(matxInv)
