def calcular_soma_quadrados(vetor):

    vetorQuadrado = []
    for i in range(len(vetor)):
        vetorQuadrado.append((vetor[i] * vetor[i]))

    soma = 0
    for i in range(len(vetorQuadrado)):
        soma += vetorQuadrado[i]


    print(soma)

vetor = [1,2,3,4,5,6,7,8,9,10]
calcular_soma_quadrados(vetor)