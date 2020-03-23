from calculation.sum import acumulator

#funcao de criacao do vetor para os valores de x e fx
def criaVetor(n):
    vetor = list()
    for i in range(0, n):
        vetor.append(float(input(f'Digite um numero para o {i + 1}o elemento: ')))
    print("")
    return(vetor)


#funcao de criacao do vetor para os valores de alpha (α)
def criaVetorAlpha(n):
    vetor = list()
    vet_aux = list()
    letra = 'α'
    for i in range(0, n):
        string_i = str(i + 1)
        conc = letra + string_i
        vet_aux.append(conc)
        vetor.append(vet_aux[:])
        vet_aux.clear()
    #print("")
    return(vetor)


#funcao de criacao da vetor que armazenara os valores de ∑((xfx)^n) e os incrementos seguintes
def criaVetorFx(n, vX, vFx):
    vetor = list() #declaro a matriz
    vet_aux = list() #declaro um vetor auxiliar para a alocacao temporaria dos valores
    for l in range(0, n):
        soma = acumulator.somaFx(n, vX, vFx, l)
        vet_aux.append(soma)
        vetor.append(vet_aux[:]) #criacao do vetor linha auxiliar, com valores zerados
        vet_aux.clear() #apago os valores no vetor auxiliar
    return(vetor)
