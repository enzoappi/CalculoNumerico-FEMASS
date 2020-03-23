#funcao de somatorio dos valores de x (∑(x))
def somaX(n, vetor, o):
    resultado = 0.0
    for i in range(0, n):
        resultado += pow(vetor[i], o)
    return(resultado)


#funcao de somatorio dos valores de x (∑(xfx))
def somaFx(n, vetorA, vetorB, o):
    resultado = 0.0
    for i in range(0, n):
        if o == 0:
            resultado += vetorB[i]
        else:
            resultado += (pow(vetorA[i], o) * vetorB[i])
    return (resultado)
