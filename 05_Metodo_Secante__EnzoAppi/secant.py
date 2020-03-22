from __future__ import division
from sympy import *

init_printing()
x, y = symbols('x y') #define x e y como variáveis simbólicas.

def f(x):
  return (cos(x) - x)


def Secante(a, b):

  while((f(a)) * (f(b)) > 0):
    print(f'\nErro!\nCom os valores {a} e {b}, nao tem-se raizes para a funcao!')
    a = float(input('\nDigite outro valor para a: '))
    b = float(input('Digite outro valor para b: '))

  erro = 0.0001 #Margem de tolerancia
  i = 0

  while True:
    i += 1
    print(f'\n\nLoop = {i}')
    print(f'f(a) = {f(a):.4f}')
    print(f'f(b) = {f(b):.4f}')
    x_plus_one = b - ((f(b) * (b - a)) / (f(b) - f(a)))
    print(f'xn+1 = {x_plus_one:.4f}')
    modulo_x_plus_one = abs(f(x_plus_one))
    print(f'|f(xn+1)| = {modulo_x_plus_one:.4f}')
    if modulo_x_plus_one < erro:
      break
    a = b
    print(f'a < - xn - 1 = {a:.4f}')
    print(f'f(a) = {f(a):.4f}')
    b = x_plus_one
    print(f'b < - xn = {b:.4f}')
    print(f'f(b) = {f(b):.4f}')

  print(f'\n\nA raiz da funcao f(x) = cos(x) - x eh {x_plus_one:.4f} com tolerancia de {erro:.4f} em {i} iteracao(oes)')
