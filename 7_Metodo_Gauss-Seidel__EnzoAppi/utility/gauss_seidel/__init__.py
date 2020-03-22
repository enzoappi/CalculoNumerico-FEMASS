import math

# Funcao para o METODO GAUSS-SEIDEL:
def Gauss_Seidel(matriz, vetor1, vetor2, num):
    vetor_aux = list()
    cont = 0
    erro = 0.05
    while True:
        cont += 1
        vetor_aux = vetor2[:]
        for l in range(0, num):
            soma = 0
            for c in range(0, num):
                if c != l:
                    soma = soma + matriz[l][c] * vetor2[c] / matriz[l][l]
            vetor2[l] = vetor1[l] / matriz[l][l] - soma

        # Calculando o teste do criterio de parada:

        vetorDIF = list()
        # Loop para o calculo de diferenca dos elementos dos vetores solucao:
        for i in range(0, num):
            dif = vetor2[i] - vetor_aux[i]
            vetorDIF.append(dif)

        # calculo da razao de convergencia do valor da solucao do vetor 2 (X - CHUTE):
        solucaoX = math.fabs(max(vetorDIF)) / math.fabs(max(vetor2))

        # verificacao de convergencia do valor solucao
        if solucaoX < erro:
            print(f'\n\nSolucao do Sistema, com margem de erro {erro}:\nVetor X = {vetor2} com {cont} iteracao(oes)!')
            break
        else:
            vetor_aux.clear()
