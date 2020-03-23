from numpy import array
from numpy import delete
from numpy import s_

#Funcao para o Calculo dos termos do polinomio
def prodMatricial(matriz, vetor):
    matxInv = array(matriz)
    vetFx = array(vetor)
    vetFx = delete(vetFx, s_[len(matriz):], 0)
    result = list()
    for l in range(0, len(matxInv)):
        a = 0.0
        for c in range(0, len(vetFx)):
            a += matxInv[l][c] * vetFx[c][0]
        result.append(a)
    return(result)
