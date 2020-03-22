def funcaoOrig(x):
    return ((pow(x, 4)) - (26 * pow(x, 2)) + (24 * x) + 21)


def raizFuncao(a, b):
    erro = 0.1
    cont = 0

    while ((funcaoOrig(a)) * (funcaoOrig(b)) > 0):
        print(f'\nErro!\nCom os valores {a} e {b}, nao tem-se raizes para a funcao!')
        a = float(input('\nDigite outro valor para a: '))
        b = float(input('Digite outro valor para b: '))

    while True:
        fa = funcaoOrig(a)
        fb = funcaoOrig(b)
        x = (a * fb - b * fa) / (fb - fa)
        fx = funcaoOrig(x)
        if x * fx < 0:
            b = x
        else:
            a = x
        cont += 1
        if fx < erro:
            break
    print(f'\nA raiz da funcao eh: {x:.4f} com erro {erro} com {cont} iteracoes')
