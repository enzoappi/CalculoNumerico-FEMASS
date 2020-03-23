#Funcao de calculo dos residuos
def calculaResiduo(vetorA, vetorB, vetorC):
    vetPol = list()
    vetDifRes = list()
    for l in range(0, len(vetorC)):
        vetorC[l] = round(vetorC[l], 4)
    for i in range(0, len(vetorA)):
        acum_polinomio = 0.0
        for j in range(0, len(vetorC)):
            acum_polinomio += vetorC[j] * pow(vetorA[i], j)
        vetPol.append(acum_polinomio)
    for i in range(0, len(vetorB)):
        vetDifRes.append(round((vetorB[i] - vetPol[i]), 4))
    return(vetDifRes)
