'''

4) (2,5 Pontos) Uma matriz pode ser considerada equilibrada quando a soma dos itens
de suas linhas (independentes) é igual a soma dos itens das suas colunas. Crie uma
função que receba uma matriz (representada como lista de listas) e retorne True ou
False caso seja ou não uma matriz equilibrada.
Ex:
[[2,7,6],
[9,5,1],
[4,3,8]] => True
2+7+6 = 15 | 9+5+1 = 15 | 4+3+8 = 15 (linhas)
2+9+4 = 15 | 7+5+3 = 15 | 6+1+8 = 15 (colunas)



'''
#feitoooooooo aaaa olha com carinho

def matriz (m):
    a=len(m[0])
    cont=0
    cont2=0
    cont4=0
    soma=0
    contadorvertical=0
    primeirasomahorizontal=0
    primeirasomavertical=0
    somavertical=0
    while cont < a:
        for i in m[cont]:
            soma += i 
        
        primeirasomahorizontal=soma #faz as somas de toda as tabelas horizontais
        soma=0
        cont+=1
        while cont2 < len(m):
            cont4=0
            while cont4 < len(m):
                somavertical += +m[cont2][cont4]    #aqui vai verificar as somas das verticais
                cont4+=1
                cont2+=1
        if somavertical == primeirasomahorizontal:  #se for igual é Vapo
            return True
        else:
            return False









print(matriz([[2,7,6],
              [9,5,1],
              [4,3,8]]))


