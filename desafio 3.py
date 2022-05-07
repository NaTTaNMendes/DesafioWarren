import time                                                     #Feito por Nattan Mendes Tinonin
                                                                #07/05/2022

resultado = []                                                  #Lista onde serão armazenadas as combinações possíveis temporariamente
saida = []                                                      #Lista onde serão armazenadas as combinações possíveis permanentemente

def mensagemErro():                                             #Mensagem mostrada caso o usuário não insira as informações corretamente
    print("Erro: o valor informado não é válido")
    time.sleep(1.5)
    print("\n" * 130)

def combinacoesPossiveis(n, indice, resultado):                 #Verifica todas as combinações possíveis para um determinado número n
    if (n == 0):                                                #n = número alvo
        print(resultado)                                        #indice = valor que será usado pelo programa para não repetir verificações já feitas (deve iniciálo com 0)
        combinacao = ""                                         #resultado = lista onde os resultados serão armazenados temporariamente (deve ser uma lista vazia)
        combinacao += str(resultado)
        saida.append(combinacao)                                #Adiciona as combinações na lista permanente    
        return 

    if (n < 0):                                                 #Proteção de segurança caso n seja negativo
        return

    for i in range(indice, len(vetor)):                         #Percorre o vetor com os valores, sempre reduzindo a quantidade para não realizar operações repetidas     
        valor = vetor[i]
        if (n >= valor):
            resultado.append(valor)
            combinacoesPossiveis(n - valor, i, resultado)       #Utiliza recursividade para percorrer todas as combinações possíveis
            resultado.pop()                                     #Remove o valor que não será utilizado da lista temporária

while True:                                                     #Recebe o n do usuário
    try:
        n = int(input("Informe o número: "))
        break
    except ValueError:
        mensagemErro()

vetor = []
while True:                                                     #Recebe os valores do usuário
    try:
        numero = input("Informe um valor para o vetor (Enter para parar): ")
        if (numero == ""):
            break
        numero = int(numero)
        vetor.append(numero)
    except ValueError:
        mensagemErro()

print()
print("Todas as combinações possíveis: ")                       #Imprime todas as combinações válidas
try:
    combinacoesPossiveis(n, 0, resultado)

    menorNumero = len(saida[0])
    for i in saida:
        if (len(i) < menorNumero):
            menorNumero = len(i)

    print()
    print("Menores combinações possíveis: ")                    #Imprime as menores combinações possíveis

    for i in saida:
        if (len(i) == menorNumero):
            print(i)
except RecursionError:
    print("Nenhuma combinação possível")
except IndexError:
    print("Nenhuma combinação possível")
