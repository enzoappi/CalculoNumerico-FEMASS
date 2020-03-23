from copy import deepcopy

#Funcao para mostrar de forma polinomial
def mostraPolinomio(vetor):
    vetorPolinomio = deepcopy((vetor))
    print('\nEm forma de POLINOMIO:')
    for i in range(0, len(vetor)):
        if i == 0:
            vetorPolinomio[i] = str(round(vetor[i], 4))
        else:
            letraNum = str(i)
            potLetraNum = '(x^' + letraNum + ')'
            vetorPolinomio[i] = str(round(vetor[i], 4)) + potLetraNum
    for p, v in enumerate(vetorPolinomio):
        if p == 0:
            print(f'({v}) ', end='')
        else:
            print(f'+ ({v}) ', end='')
    print('')
