def showFinalMtx(vetor, matriz):
    for l in range(0, len(matriz)):
        print(f'| {vetor[l]:^7} | ', end='')
        for c in range(0, len(matriz)):
            if c == len(matriz) - 1:
                print(f'{matriz[l][c]:^7} |')
            else:
                print(f'{matriz[l][c]:^7}  ', end='')
