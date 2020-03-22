#Criando o teste de convergencia 1 (Matriz Diagonal dominante):
def convergencia_1(matriz, num):
  linha = 1
  coluna = 1
  #Testando a convergencia por linhas
  for l, v in enumerate(matriz):
    soma = 0
    for c, v in enumerate(matriz[l]):
      if c != l:
        soma = soma + v;
    #Caso o teste de Matriz Dominante por linhas seja falso. (em qualquer delas):
    if matriz[l][l] < soma:
      print('\nO Sistema NAO EH Matriz Dominante por LINHAS!')
      linha = 0
      break
  #inicio do teste de convergencia, de Matriz dominante POR COLUNAS
  if linha == 0:
    print('\n\nVamos testar a convergencia, do Sistema, por colunas...')
    for c in range(0, num):
      soma = 0
      for l, v in enumerate(matriz):
        if l != c:
          soma = soma + matriz[l][c]
      #Caso o teste de Matriz Dominante por colunas seja falso. (em qualquer delas):
      if matriz[c][c] < soma:
        print('\nO Sistema NAO EH Matriz Dominante por COLUNAS!')
        coluna = 0
        break
  if linha == 0 and coluna == 0:
    print('\n\n\nO Sistema digitado, NAO tem CONVERGENCIA!\n\nTeste outro, por gentileza!')
    return(0)
  else:
    print('\n\nO Sistema eh diagonal dominante!\nVamos prosseguir para o uso do 2º criterio de convergencia!')
    return(1)
