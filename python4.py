#crie uma função que calcule a área de um retângulo

def retangulo (l1, l2):
    t = l1*l2
    if t <= 0:
        return 'não é um retangulo, valor negativo'
    else:
        return t
    
print(retangulo(-0,-2))
    