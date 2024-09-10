def calcular_cpf():
    cpf = input("digite o cpf: ")

    cpf_sem_ponto = cpf.replace(".", "")
    cpf_final = cpf_sem_ponto.replace("-", "")

    soma = 0
    for i in range(len(cpf_final)):
        soma += int(cpf_final[i])


    if(soma % 2 == 0):
        print(soma)
        print("o cpf é PAR")
    else:
        print(soma)
        print("o cpf é ÍMPAR")

calcular_cpf()