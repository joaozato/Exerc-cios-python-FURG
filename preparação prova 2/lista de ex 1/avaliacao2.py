def collatz (n):
    lista=[]
    cont=0
    maiornumber=0
    while n > 1:
        if n %2 == 0:
            a = n//2
            lista.append(a)
            n=a
            cont+=1
        else:
            b= (n *3)+1
            lista.append(b)
            n=b
            cont+=1
        if n > maiornumber:
            maiornumber=n
    return "o maior numero é ",maiornumber, "e foram contabilizados ",cont,"numeros" ,lista 


print(collatz(127))


