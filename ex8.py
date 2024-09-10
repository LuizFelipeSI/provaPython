def calcularMedia():
    notas = [7,5,3,5]
    soma = notas[0] + notas[1] + notas[2] + notas[3]

    media = soma / 4
    print(media)

    if(media > 6):
        print("APROVADO")
    else:
        notas.append(8)
        notaComProvaFinal = soma + notas[4]
        media = notaComProvaFinal / 5
        if(media > 4):
            print("APROVADO")
        else:
            print("REPROVADO")

    print(media)

calcularMedia()