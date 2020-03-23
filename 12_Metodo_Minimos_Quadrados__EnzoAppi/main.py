from creation import vector
from creation import matrix
from creation import invmatrix
from presentation import systems
from presentation import result
from presentation import polyfun
from calculation.polynomial import terms
from calculation.error import residual
from calculation.error import sqr_res

#PROGRAMA PRINCIPAL
n = int(input('Digite a quantidade de pontos no Metodo Minimos Quadrados: '))
while n < 0:
    n = int(input('\nNumero invalido!\nDigite a quantidade de pontos no Metodo Minimos Quadrados: '))
vetX = vector.criaVetor(n) #instanciacao de x como vetX
vetFx = vector.criaVetor(n) #instanciacao de fx como vetFx
Alpha = vector.criaVetorAlpha(n) #instanciacao de alpha como Alpha
A = matrix.criaA(n, vetX) #montando a matriz A
fx = vector.criaVetorFx(n, vetX, vetFx) #montando o vetor resposta
ordem = int(input('Digite a ordem do polinomio desejado no Metodo Minimos Quadrados: '))
systems.mostraSistema(ordem + 1, A, Alpha, fx) #Sistema a ser resolvido
A_inv = invmatrix.criaMatrizInversa(ordem + 1, A) #instanciacao da matriz inversa
systems.mostraSistema2(ordem + 1, A_inv, Alpha, fx) #Sistema a ser resolvido
termosPolinomio = terms.prodMatricial(A_inv, fx)
result.imprimeResultado(ordem + 1, Alpha, termosPolinomio) #Disponibilizacao do resultado final do Sistema
polyfun.mostraPolinomio(termosPolinomio)
phi = residual.calculaResiduo(vetX, vetFx, termosPolinomio)
print(f'\nErros Residuais: {phi}')
print(f'\n∑r^2(xi) = {round(sqr_res.somaErroQuadrado(phi), 4)}')
