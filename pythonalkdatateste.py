D=int(input('Digite um dia'))
M=int(input('Digite um Mês'))
A=int(input('Digite o ano'))
N=int(input('Digite o número de dias para avançar'))

while N > 0:
    if M == 4 or M == 6 or M == 9 or M == 11:
        X = 30
    if M == 2:
        X=28
    else:
        X=31

    D +=1
    N-=1

    if D>X:
        M+=1
        D=1
    if M>12:
        M=1
        A+=1
print (f'a data futura é {D}/{M}/{A}')
    
