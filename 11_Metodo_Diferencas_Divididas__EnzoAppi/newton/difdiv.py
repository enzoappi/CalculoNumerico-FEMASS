def mtdDifDiv(vetor, matriz):
  for c in range(0, len(matriz)):
    for l in range(0, len(matriz) - c):
      if c != 0:
        matriz[l][c] = ((matriz[l + 1][c - 1] - matriz[l][c - 1]) / (vetor[l + c] - vetor[l]))
  return(matriz)
