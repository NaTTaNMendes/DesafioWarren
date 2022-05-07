n = 0                                   #Feito por Nattan Mendes Tinonin
                                        #05/05/2022
while True:
    reverso = int(str(n)[::-1])         #Inverte o inteiro
    if ((n + reverso) > 1000000):       #Verifica se não passa o limite
        break
    if ((reverso + n) % 2 == 1):        #Verifica se é ímpar
        print(n)                        #Imprime o valor
    n += 1