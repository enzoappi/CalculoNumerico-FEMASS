def criaFx(n):
    fx = list() #declaro a matriz
    provFx = list() #declaro um vetor auxiliar para a alocacao temporaria dos valores
    for i in range(0, n):
        for j in range(0, n):
            provFx.append('-') #criacao do vetor linha auxiliar, com valores zerados
        fx.append(provFx[:]) #adicionando na i-esima linha de fx os valores do vetor aux.
        provFx.clear() #apago os valores no vetor auxiliar
    print('\n')
    for k in range(0, n): #criando um loop para pedir ao usuario, os valores de fx
      #Alocando os valores do usuario, na coluna 0 da matriz fx
        fx[k][0] = (float(input(f'Digite um numero para o {k + 1}o fx: ')))
    return(fx)
