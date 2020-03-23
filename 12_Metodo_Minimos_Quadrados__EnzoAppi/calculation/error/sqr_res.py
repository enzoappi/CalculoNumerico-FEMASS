#Somatorio dos erros residuais quadrados (phi^2)
def somaErroQuadrado(vetor):
    acum_erros = 0.0
    for i in range(0, len(vetor)):
        acum_erros += pow(vetor[i], 2)
    return(acum_erros)
