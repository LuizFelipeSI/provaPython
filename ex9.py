def fibonacci_sequence(N):
    vetor = [0,1]
    while(len(vetor) < N):
        vetor.append(vetor[len(vetor)-1] + vetor[len(vetor)-2])

    print(vetor)

fibonacci_sequence(7)