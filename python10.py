'''
Escreva uma função chamada calcular_conceito que receba uma nota (de 0 a 10) e retorne o conceito correspondente em string, de acordo com a seguinte tabela:

Nota 9.0 a 10.0: "A" (Excelente)

Nota 7.0 a 8.9: "B" (Bom)

Nota 5.0 a 6.9: "C" (Regular)

Abaixo de 5.0: "D" (Reprovado)

Nome da função: calcular_conceito

Parâmetro: nota (número)

Retorno: Uma string com o conceito.

'''
def calcular (nota):
    if nota >= 9 and nota <=10:
        return 'Conceito A (Excelente)'
    if nota >=7 and nota <=8.9:
        return 'Conceito B (bom)'
    if nota >=5 and nota <=6.9:
        return 'Conceito C (Regular)'
    else:
        return 'Conceito D (Reprovado)'
    
print(calcular(6.7))