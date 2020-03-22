def funcaoOrig(x):
  return(x - 2)

def raizFuncao(a, b):
  erro = 0.1
  cont = 0
  while((funcaoOrig(a)) * (funcaoOrig(b)) >= 0):
    print(f'\nErro!\nCom os valores {a} e {b}, eh impossivel calcularmos as raizes da funcao original!')
    a = float(input('\nDigite outro valor para a: '))
    b = float(input('Digite outro valor para b: '))
  while(abs(a - b) > erro):
    x = (a + b) / 2
    if((funcaoOrig(a)) * (funcaoOrig(x)) < 0):
      b = x
    else:
      a = x
    cont += 1
  print(f'\nA raiz da funcao eh: {x} com precisao de {erro} em {cont} iteracoes')
