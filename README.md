# DesafioWarren


## Como rodar os códigos

Para rodar o programa o usuário deve ter algum compilador python instalado na máquina, sendo necessário a utilização do terminal para digitar e receber os dados.

* Link para o download do python 3: https://www.python.org/downloads/
* Link para o download do VSCode: https://code.visualstudio.com/

## Tecnologias utilizadas

 * Python 3
 * Visual Studio Code

## - DESAFIO 1 -

Enunciado:

Alguns números inteiros positivos n possuem uma propriedade na qual a soma de n + reverso(n) resultam em números ímpares. Por exemplo, 36 + 63 = 99 e 409 + 904 = 1313. Considere que n ou reverso(n) não podem começar com 0.

Existem 120 números reversíveis abaixo de 1000.

Construa um algoritmo que mostre na tela todos os números n onde a soma de n + reverso(n) resultem em números ímpares que estão abaixo de 1 milhão.

### Aplicação:

O programa irá imprimir na tela todos os números reversos onde a soma (numero + reverso) < 1000000

**OBS**
Aparentemente o enunciado possui um erro, já que existem mais de 120 números reversíveis abaixo de 1000.


## - DESAFIO 2 -

Um professor de programação, frustrado com a falta de disciplina de seus alunos, decidi cancelar a aula se menos de x alunos estiverem presentes quando a aula for iniciada. O tempo de chegada varia entre:

Normal: tempoChegada <= 0
Atraso: tempoChegada > 0
Construa um algoritmo que dado o tempo de chegada de cada aluno e o limite x de alunos presentes, determina se a classe vai ser cancelada ou não ("Aula cancelada” ou “Aula normal”).

Exemplo:

Entrada de dados:
x = 3
tempoChegada = [-2, -1, 0, 1, 2]

Saída de dados:
Aula normal.

Explicação:
Os três primeiros alunos chegaram no horário. Os dois últimos estavam atrasados. O limite é de três alunos, portanto a aula não será cancelada.

### Aplicação: 

O programa somente aceitará números inteiros do usuário, informando ao final a se a aula deve ou não ser cancelada.

## - DESAFIO 3 - 

Dado um vetor de números e um número n. Determine a soma com o menor número de elementos entre os números do vetor mais próxima de n e também mostre os elementos que compõem a soma. Para criar a soma, utilize qualquer elemento do vetor uma ou mais vezes.

Exemplo:

Entrada de dados:

N = 10
V = [2, 3, 4]

Saída de dados:

10
[2, 4, 4]
[3, 3, 4]

Explicação:

Se N = 10 e V = [2, 3, 4] você pode utilizar as seguintes soma: [2, 2, 2, 2, 2], [2, 2, 3, 3], [2, 4, 4] ou [3, 3, 4]. Como a quantidade de elementos em [2, 4, 4] e [3, 3, 4] é igual, os dois conjuntos devem ser mostrados.

### Aplicação

O programa somente aceitará números inteiros do usuário, mostrando ao final todas as combinações possíveis e as menores separadamente.
