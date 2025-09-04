'''
Questão 3 (3,5 Pontos)

Crie um programa em Python que leia um número inteiro e escreva a soma dos números correspondentes a cada dígito do número. Por exemplo:

Número	Soma
1412	8
4341220	16
101	    2
Nesta questão, você não pode utilizar strings. Deve utilizar operações matemáticas que vimos em aula, como o resto e a divisão inteira.


'''

N= int(input('Digite um numero inteiro e eu vou ler a soma dele'))
N2=str(N)
cont= 0
a=0
for i in N2:
    a += int(N2[cont])
    cont+=1
print(a)


