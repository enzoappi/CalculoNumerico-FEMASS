import original

def funcao_Integral(a, b, n):
  h = (b - a) / n
  soma_Trapz = (original.funcao_Original(a) + original.funcao_Original(b)) / 2
  print(f'\nO valor acumulado {soma_Trapz}')
  for i in range(1, n):
      soma_Trapz += original.funcao_Original(a + (i * h))
      print(f'\nO valor acumulado {soma_Trapz}')
  Area_total = h * soma_Trapz
  print(f'\n\nO valor da integral eh {Area_total}')
