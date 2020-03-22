from numpy import poly1d

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
