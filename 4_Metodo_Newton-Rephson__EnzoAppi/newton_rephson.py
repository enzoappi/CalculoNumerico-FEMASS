from __future__ import division
from sympy import *

init_printing()
x, y = symbols('x y') #define x e y como variáveis simbólicas.

def f(x):
  return ((pow(x, 3) - 5 * pow(x, 2) + x + 3))

def drv_f(a):
  return(diff(f(x), x).subs(x, a)) #calculando a derivada da funcao definida no ponto a

def NewtonRephson(a, b):

  while((f(a)) * (f(b)) > 0):
    print(f'\nErro!\nCom os valores {a} e {b}, nao tem-se raizes para a funcao!')
    a = float(input('\nDigite outro valor para a: '))
    b = float(input('Digite outro valor para b: '))

  #der_func = der_f(a) calculando a derivada da funcao
  #print(der_func)

  erro = 0.01 #Margem de tolerancia
  i = 0

  while True:
    i += 1
    x = a - (f(a) / drv_f(a))
    xn = abs(f(x))
    if xn < erro:
      break
    a = x

  print(f'\n\nA raiz da funcao f(x) = x^3 - 5x^2 + x + 3 eh {x:.4f} com tolerancia de {erro:.2f} em {i} iteracao(oes)')
