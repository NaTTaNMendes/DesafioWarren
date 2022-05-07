import time                                                     #Feito por Nattan Mendes Tinonin
                                                                #05/05/2022

def mensagemErro():                                             #Mensagem mostrada caso o usuário não insira as informações corretamente
    print("Erro: o valor informado não é válido")
    time.sleep(1.5)
    print("\n" * 130)

while True:                                                     #Coleta a quantidade máxima de atrasados
    try:
        limite = int(input("Informe a quantidade máxima de alunos atrasados: "))
        break
    except ValueError:
        mensagemErro()
tempos = []
while True:                                                     #Coleta os horários de chegada dos alunos
    while True:
        try:    
            tempo = int(input("Informe o tempo do aluno: "))
            break
        except ValueError:
            mensagemErro()
    tempos.append(tempo)
    continuar = input("Digite qualquer enter para continuar (qualquer outra tecla para sair): ")
    print("\n" * 130)
    if (continuar != ""):
        break

atrasados = 0
for posicao in tempos:                                          #Processa a quantidade de alunos atrasados    
    if (posicao > 0):
        atrasados += 1

if (atrasados <= limite):                                       #Responde se a aula deve ou não ser cancelada
    print("Aula normal")
else:
    print("Aula cancelada")