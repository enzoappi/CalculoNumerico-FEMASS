from numpy import linalg
from numpy import array
from numpy import s_
from numpy import delete
from copy import deepcopy

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


#funcao de somatorio dos valores de x (∑(x))
def somaX(n, vetor, o):
    resultado = 0.0
    for i in range(0, n):
        resultado += pow(vetor[i], o)
    return(resultado)


#funcao de somatorio dos valores de x (∑(xfx))
def somaFx(n, vetorA, vetorB, o):
    resultado = 0.0
    for i in range(0, n):
        if o == 0:
            resultado += vetorB[i]
        else:
            resultado += (pow(vetorA[i], o) * vetorB[i])
    return (resultado)


#funcao de criacao da matriz que armazenara os valores de ∑(x^n) e os incrementos seguintes
def criaA(n, vX):
    matriz = list() #declaro a matriz
    mat_aux = list() #declaro um vetor auxiliar para a alocacao temporaria dos valores
    for l in range(0, n):
        for c in range(0, n):
            if l == 0 and c == 0:
                mat_aux.append(n)
            elif l == 0 and c > 0:
                soma = somaX(n, vX, c)
                mat_aux.append(soma)
            elif l > 0 and c == 0:
                soma = somaX(n, vX, l)
                mat_aux.append(soma)
            else:
                #if l == c:
                soma = somaX(n, vX, (l + c))
                mat_aux.append(soma)
        matriz.append(mat_aux[:]) #criacao do vetor linha auxiliar, com valores zerados
        mat_aux.clear() #apago os valores no vetor auxiliar
    return(matriz)


#funcao de criacao da vetor que armazenara os valores de ∑((xfx)^n) e os incrementos seguintes
def criaVetorFx(n, vX, vFx):
    vetor = list() #declaro a matriz
    vet_aux = list() #declaro um vetor auxiliar para a alocacao temporaria dos valores
    for l in range(0, n):
        soma = somaFx(n, vX, vFx, l)
        vet_aux.append(soma)
        vetor.append(vet_aux[:]) #criacao do vetor linha auxiliar, com valores zerados
        vet_aux.clear() #apago os valores no vetor auxiliar
    return(vetor)


#Funcao que mostra o sistema a ser resolvido
def mostraSistema(ordem, matriz, vetorA, vetorB):
    print('\nSISTEMA FORMADO por ---> (mat(A) * vet(α) = mat(fx)) :\n')
    for l in range(0, ordem):
        print(f'|', end='')
        for c in range(0, ordem):
            print(f' {matriz[l][c]:^12.4f}', end='')
        if ordem % 2 != 0:
            if l == (ordem - 1) / 2:
                print(f' | * |{vetorA[l][0]}| = |{vetorB[l][0]:^12.4f}|')
            else:
                print(f' |   |{vetorA[l][0]}|   |{vetorB[l][0]:^12.4f}|')
        else:
            if l == ((ordem / 2) - 1):
                print(f' | * |{vetorA[l][0]}| = |{vetorB[l][0]:^12.4f}|')
            else:
                print(f' |   |{vetorA[l][0]}|   |{vetorB[l][0]:^12.4f}|')


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


#Funcao que mostra o sistema a ser resolvido
def mostraSistema2(ordem, matriz, vetorA, vetorB):
    print('\nSISTEMA A SER RESOLVIDO ---> (vet(α) = mat(fx) * mat(A_inv) :\n')
    for l in range(0, ordem):
        if ordem % 2 != 0:
            if l == (ordem - 1) / 2:
                print(f'|{vetorA[l][0]}| = |', end='')
            else:
                print(f'|{vetorA[l][0]}|   |', end='')
        else:
            if l == ((ordem / 2) - 1):
                print(f'|{vetorA[l][0]}| = |', end='')
            else:
                print(f'|{vetorA[l][0]}|   |', end='')
        for c in range(0, ordem):
            if ordem % 2 != 0:
                if c != (ordem - 1):
                    print(f' {matriz[l][c]:^12.4f} ', end='')
                else:
                    if l == (ordem - 1) / 2:
                        print(f' {matriz[l][c]:^12.4f}| * ', end='')
                    else:
                        print(f' {matriz[l][c]:^12.4f}|   ', end='')
            else:  # se a ordem for um numero PAR
                if l == ((ordem / 2) - 1):
                    if c == ordem - 1:
                        print(f' {matriz[l][c]:^12.4f}| * ', end='')
                    else:
                        print(f' {matriz[l][c]:^12.4f} ', end='')
                else:
                    if c == ordem - 1:
                        print(f' {matriz[l][c]:^12.4f}|   ', end='')
                    else:
                        print(f' {matriz[l][c]:^12.4f} ', end='')
        print(f'|{vetorB[l][0]:^12.4f}|')


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


#Funcao para imprimir o resultado final do Sistema
def imprimeResultado(ordem, matriz, vetor):
    print('\nRESULTADO FINAL DO SISTEMA:\n')
    for l in range(0, ordem):
        if ordem % 2 != 0:
            if l == (ordem - 1) / 2:
                print(f'|{matriz[l][0]}| = |{vetor[l]:^12.4f}|')
            else:
                print(f'|{matriz[l][0]}|   |{vetor[l]:^12.4f}|')
        else:
            if l == ((ordem / 2) - 1):
                print(f'|{matriz[l][0]}| = |{vetor[l]:^12.4f}|')
            else:
                print(f'|{matriz[l][0]}|   |{vetor[l]:^12.4f}|')


#Funcao para mostrar de forma polinomial
def mostraPolinomio(vetor):
    vetorPolinomio = deepcopy((vetor))
    print('\nEm forma de POLINOMIO:')
    for i in range(0, len(vetor)):
        if i == 0:
            vetorPolinomio[i] = str(round(vetor[i], 4))
        else:
            letraNum = str(i)
            potLetraNum = '(x^' + letraNum + ')'
            vetorPolinomio[i] = str(round(vetor[i], 4)) + potLetraNum
    for p, v in enumerate(vetorPolinomio):
        if p == 0:
            print(f'({v}) ', end='')
        else:
            print(f'+ ({v}) ', end='')
    print('')


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


#Somatorio dos erros residuais quadrados (phi^2)
def somaErroQuadrado(vetor):
    acum_erros = 0.0
    for i in range(0, len(vetor)):
        acum_erros += pow(vetor[i], 2)
    return(acum_erros)

#PROGRAMA PRINCIPAL
n = int(input('Digite a quantidade de pontos no Metodo Minimos Quadrados: '))
while n < 0:
    n = int(input('\nNumero invalido!\nDigite a quantidade de pontos no Metodo Minimos Quadrados: '))
vetX = criaVetor(n) #instanciacao de x como vetX
vetFx = criaVetor(n) #instanciacao de fx como vetFx
Alpha = criaVetorAlpha(n) #instanciacao de alpha como Alpha
A = criaA(n, vetX) #montando a matriz A
fx = criaVetorFx(n, vetX, vetFx) #montando o vetor resposta
ordem = int(input('Digite a ordem do polinomio desejado no Metodo Minimos Quadrados: '))
mostraSistema(ordem + 1, A, Alpha, fx) #Sistema a ser resolvido
A_inv = criaMatrizInversa(ordem + 1, A) #instanciacao da matriz inversa
mostraSistema2(ordem + 1, A_inv, Alpha, fx) #Sistema a ser resolvido
termosPolinomio = prodMatricial(A_inv, fx)
imprimeResultado(ordem + 1, Alpha, termosPolinomio) #Disponibilizacao do resultado final do Sistema
mostraPolinomio(termosPolinomio)
phi = calculaResiduo(vetX, vetFx, termosPolinomio)
print(f'\nErros Residuais: {phi}')
print(f'\n∑r^2(xi) = {round(somaErroQuadrado(phi), 4)}')
