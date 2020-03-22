#Criando a Matriz A
def CriarMatriz(a, b):
  matriz = list()
  provisorio = list()
  print('\n')
  for i in range(0, a):
    for j in range(0, a):
      provisorio.append(int(input(f'Digite um numero para o elemento {b}{i + 1}{j + 1}: ')))
      if j == a - 1:
        matriz.append(provisorio[:])
    provisorio.clear()
  print(f'\n\nMatriz {b} = {matriz}')
  return(matriz)
