import original

def funcao_Integral(a, b, n):
  while(n % 2 != 0):
    n = int(input('\nValor invalido!\nDigite um valor PAR, para n: '))
  h = (b - a) / n
  soma_Trapz = (original.funcao_Original(a) + original.funcao_Original(b))
  print(f'\nO valor acumulado {soma_Trapz}')
  for i in range(1, n):
    print(f'\nLoop {i}')
    if i % 2 == 0:
      soma_Trapz += 2 * (original.funcao_Original(a + (i * h)))
    else:
      soma_Trapz += 4 * (original.funcao_Original(a + (i * h)))
    print(f'\nO valor acumulado {soma_Trapz}')
  Area_total = (h * soma_Trapz) / 3
  print(f'\n\nO valor da integral eh {Area_total}')
