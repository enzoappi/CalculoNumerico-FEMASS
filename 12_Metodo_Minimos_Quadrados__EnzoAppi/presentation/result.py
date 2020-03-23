#Funcao para imprimir o resultado final do Sistema
def imprimeResultado(ordem, matriz, vetor):
    print('\nRESULTADO FINAL DO SISTEMA:\n')
    for l in range(0, ordem):
        if ordem % 2 != 0:
            if l == (ordem - 1) / 2:
                print(f'|{matriz[l][0]}| = |{vetor[l]:^12.4f}|')
            else:
                print(f'|{matriz[l][0]}|   |{vetor[l]:^12.4f}|')
        else:
            if l == ((ordem / 2) - 1):
                print(f'|{matriz[l][0]}| = |{vetor[l]:^12.4f}|')
            else:
                print(f'|{matriz[l][0]}|   |{vetor[l]:^12.4f}|')
