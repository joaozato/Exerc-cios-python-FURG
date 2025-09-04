'''
1)
Enunciado:
Cada carro tem um desempenho, que é geralmente medido 
por quantos quilômetros ele pode percorrer com 1 litro de gasolina. 
Escreva um programa em Python que leia o desempenho de um carro e um 
trajeto percorrido em um mês. Escreva o quanto foi gasto em reais, considerando a gasolina a R$5,85.

Exemplo fornecido:
Desempenho: 12 km/l
Trajeto: 1000 km
Gasto: R$ 487,50 
'''

T=float(input("Quantos kilometros você rodou?"))
D=float(input('Quantos kilometros por litro ele faz?'))
G= (T/D) * 5.85
print(f"o desempenho foi {D}, o trajeto total foi {T} e o gasto foi {G:.2f}")