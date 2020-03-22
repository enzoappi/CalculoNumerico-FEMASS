def raizFuncao (a, b, c):
  if(a == 0):
    while a == 0:
      print('Valor invalido! Digite um valor maior que zero para (a)')
      a = int(input('Digite um valor para (a):'))
  else:
    delta = ((b ** 2) - (4 * a * c))
    if(delta < 0):
      print(f'\nNão existe solucao nos REAIS, para Delta: ##{delta}')
    elif(delta == 0):
      raiz = (-b / (2 * a))
      print(f'\nO valor da raiz de Delta = {delta} eh: {raiz}')
    else:
      raiz1 = ((-b + delta) / 2 * a)
      raiz2 = ((-b - delta) / 2 * a)
      print(f'\nO valor das raizes de Delta = {delta} sao: {raiz1} e {raiz2}')
