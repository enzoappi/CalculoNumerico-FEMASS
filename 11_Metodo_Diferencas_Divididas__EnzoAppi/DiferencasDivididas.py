import numpy as np
from np import poly1d
from copy import deepcopy

#funcao de criacao do vetor para os valores de x
def criaX(n):
    x = list()
    for i in range(0, n):
        x.append(float(input(f'Digite um numero para o {i + 1}o x: ')))
    return(x)


#funcao de criacao da matriz que armazenara os valores de fx e os incrementos seguintes
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


#funcao de execucao do Metodo de Newton (Diferencas Divididas)
def mtdDifDiv(vetor, matriz):
  for c in range(0, len(matriz)):
    for l in range(0, len(matriz) - c):
      if c != 0:
        matriz[l][c] = ((matriz[l + 1][c - 1] - matriz[l][c - 1]) / (vetor[l + c] - vetor[l]))
  return(matriz)


#funcao para disponibilizacao do resultado final do polinomio advindo do mtdDifDiv
def criarPolinomio(ordem, vetor, matriz):
    while ordem >= len(vetor): #teste e correcao do valor de ordem
        ordem = int(input('Digite a Ordem de interpolacao do polinomio final: '))
    Polinomio = matriz[0][0] #valor de a0
    p = 1.0 #variavel para alocar os valores (x - x[0])(x - x[1])...(x - x[n-1])
    for i in range(0, ordem):
      pIncr = poly1d([vetor[i]], True) #calculo do p-seguinte
      p *= pIncr #atualizacao de p com o p-seguinte
      Polinomio += (matriz[0][i + 1] * (p)) #incremento do polinomio com os termos de ordem seguintes
    print(f'\nPOLINOMIO FINAL = {Polinomio}\n') #OBS: no resultado a primeira linha indica os valores de ORDEM a que termos da segunda ordem estao elevados 
    #ex: POLINOMIO FINAL = 3 2 1
    # 1x + 3x - 2x + 4 -----> significa: x^3 + 3x^2 - 2x + 4
    num = float(input('Digite um numero para o valor de x: '))
    print('\nVALOR FINAL DO POLINOMIO:')
    print(f'P({num}) = {Polinomio(num)}')


#PROGRAMA PRINCIPAL
n = int(input('Digite a quantidade de pontos no Metodo Diferencas Divididas: '))
vetX = criaX(n) #instanciacao de x como vetX
matFx = criaFx(n) #instanciacao da matriz fx como matFX
matAuxFx = deepcopy(matFx) #copia temporaria, total, da matFX para matAuxFx
matFx_final = mtdDifDiv(vetX, matAuxFx) #instanciacao da matriz final como matFx_final
print('\n\nCRIADOS:\n') 
print(f'Vetor X = {vetX}\n')
print(f'Matriz Fx = {matFx}\n')
print(f'Matriz FINAL:\n')
#Disponibilizacao da Matriz Final em visual MATRICIAL (de forma usual)
for l in range(0, len(matFx_final)):
    print(f'| {vetX[l]:^7} | ', end='')
    for c in range(0, len(matFx_final)):
        if c == len(matFx_final) - 1:
            print(f'{matFx_final[l][c]:^7} |')
        else:
            print(f'{matFx_final[l][c]:^7}  ', end='')
#Disponibilizacao do resultado final do polinomio literal & numerico
criarPolinomio(int(input('\nDigite o valor da ordem do Polinomio final: ')), vetX, matFx_final)
