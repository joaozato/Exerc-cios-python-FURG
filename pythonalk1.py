n = int(input('Digite um número inteiro positivo'))
nstr =str(n)
cont =0
cont2=-1
a = ''
while cont < len(nstr):
    a += nstr[cont2]
    cont+=1
    cont2-=1
b = int(a)
print(b)

