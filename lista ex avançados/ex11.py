'''

11. Matriz Identidade
Crie uma função `matriz_identidade(n)` que receba um número inteiro `n` e retorne uma
lista de listas representando uma matriz identidade de tamanho `n`.
Exemplo:
Entrada: 3
Saída: [[1,0,0],[0,1,0],[0,0,1]]

'''

def matriz_identidade (n):
    matrizes=[]
    matrizes2=[]
    cont=0
    cont2=0
    while len(matrizes2) < n: #enquanto o len de matrizes for menor que a variavel embutida pelo usuário (N)
        while cont2 < n*n:   #enquanto contador 2 for menor que n*n (nesse caso é por que vai ser uma posição multiplicada por ela mesma, são n colunas com n espaços)
            matrizes.append(0) #ele da um append no valor zero, para preencher a tabela.
            cont2+=1     #aumenta o contador para chegar mais próximo do limite
            if len(matrizes) == n:   #aqui uma verificação de que se o len da primeira matriz for igual ao N(tamanho esperado da colunma)
                matrizes2.append(matrizes) #outra lista da append nessa primeira, fazendo assim o fechamento
                matrizes=[]  # e resetando essa matriz 
    cont2=0
    while cont2 < len(matrizes2): #aqui nós zeramos o contador 2, enquanto ele for menor que o len da lista que tem o tamanho N
        matrizes2[cont][cont]=1     #pegamos a posição da matriz que queremos, e fazemos ela receber um, bem simples.
        cont2+=1
        cont+=1

    return matrizes2
        




print(matriz_identidade(3))