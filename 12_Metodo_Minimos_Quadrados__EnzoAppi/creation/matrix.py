from calculation.sum import acumulator

#funcao de criacao da matriz que armazenara os valores de ∑(x^n) e os incrementos seguintes
def criaA(n, vX):
    matriz = list() #declaro a matriz
    mat_aux = list() #declaro um vetor auxiliar para a alocacao temporaria dos valores
    for l in range(0, n):
        for c in range(0, n):
            if l == 0 and c == 0:
                mat_aux.append(n)
            elif l == 0 and c > 0:
                soma = acumulator.somaX(n, vX, c)
                mat_aux.append(soma)
            elif l > 0 and c == 0:
                soma = acumulator.somaX(n, vX, l)
                mat_aux.append(soma)
            else:
                #if l == c:
                soma = acumulator.somaX(n, vX, (l + c))
                mat_aux.append(soma)
        matriz.append(mat_aux[:]) #criacao do vetor linha auxiliar, com valores zerados
        mat_aux.clear() #apago os valores no vetor auxiliar
    return(matriz)
