'''

14. Triângulo de Pascal
https://pt.wikipedia.org/wiki/Tri%C3%A2ngulo_de_Pascal
Crie uma função `triangulo_pascal(n)` que retorne uma lista de listas representando as
primeiras `n` linhas do triângulo de Pascal.


'''
def pascal_tri(lines):
    t= [[0 for i in range(lines)] for i in range(lines)]
    for n in range(lines):
        for k in range(lines):
            if n == 0 and k == 0:
                t[n][k] = 1
            elif n > -1 and k > -1:
                t[n][k] = t[n-1][k-1] + t[n-1][k]
    return t
    

print(pascal_tri(5))