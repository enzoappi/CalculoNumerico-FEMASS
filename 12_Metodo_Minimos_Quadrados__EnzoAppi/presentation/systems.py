#Funcao que mostra o sistema a ser resolvido
def mostraSistema(ordem, matriz, vetorA, vetorB):
    print('\nSISTEMA FORMADO por ---> (mat(A) * vet(α) = mat(fx)) :\n')
    for l in range(0, ordem):
        print(f'|', end='')
        for c in range(0, ordem):
            print(f' {matriz[l][c]:^12.4f}', end='')
        if ordem % 2 != 0:
            if l == (ordem - 1) / 2:
                print(f' | * |{vetorA[l][0]}| = |{vetorB[l][0]:^12.4f}|')
            else:
                print(f' |   |{vetorA[l][0]}|   |{vetorB[l][0]:^12.4f}|')
        else:
            if l == ((ordem / 2) - 1):
                print(f' | * |{vetorA[l][0]}| = |{vetorB[l][0]:^12.4f}|')
            else:
                print(f' |   |{vetorA[l][0]}|   |{vetorB[l][0]:^12.4f}|')

#Funcao que mostra o sistema a ser resolvido
def mostraSistema2(ordem, matriz, vetorA, vetorB):
    print('\nSISTEMA A SER RESOLVIDO ---> (vet(α) = mat(fx) * mat(A_inv) :\n')
    for l in range(0, ordem):
        if ordem % 2 != 0:
            if l == (ordem - 1) / 2:
                print(f'|{vetorA[l][0]}| = |', end='')
            else:
                print(f'|{vetorA[l][0]}|   |', end='')
        else:
            if l == ((ordem / 2) - 1):
                print(f'|{vetorA[l][0]}| = |', end='')
            else:
                print(f'|{vetorA[l][0]}|   |', end='')
        for c in range(0, ordem):
            if ordem % 2 != 0:
                if c != (ordem - 1):
                    print(f' {matriz[l][c]:^12.4f} ', end='')
                else:
                    if l == (ordem - 1) / 2:
                        print(f' {matriz[l][c]:^12.4f}| * ', end='')
                    else:
                        print(f' {matriz[l][c]:^12.4f}|   ', end='')
            else:  # se a ordem for um numero PAR
                if l == ((ordem / 2) - 1):
                    if c == ordem - 1:
                        print(f' {matriz[l][c]:^12.4f}| * ', end='')
                    else:
                        print(f' {matriz[l][c]:^12.4f} ', end='')
                else:
                    if c == ordem - 1:
                        print(f' {matriz[l][c]:^12.4f}|   ', end='')
                    else:
                        print(f' {matriz[l][c]:^12.4f} ', end='')
        print(f'|{vetorB[l][0]:^12.4f}|')
