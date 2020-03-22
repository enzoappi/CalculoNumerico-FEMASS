def criaX(n):
    x = list()
    for i in range(0, n):
        x.append(float(input(f'Digite um numero para o {i + 1}o x: ')))
    return(x)
