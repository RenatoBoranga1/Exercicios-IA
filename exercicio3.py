import math

def entropia(n1, n2):
    if n1 < 0 or n2 < 0:
        print("Quantidades inválidas!")
    elif n1 == 0 or n2 == 0:
        return 0
    else:
        p1 = n1 / (n1 + n2)
        p2 = 1 - p1
        return -p1 * math.log2(p1) - p2 * math.log2(p2)

def entropia_multi_classe(*quantidades):
    total_elementos = sum(quantidades)
    
    if total_elementos == 0:
        print('Conjunto vazio!')
        return 0
    
    soma = 0
    
    for nec in quantidades:
        if nec < 0:
            print("Quantidade inválida")
        elif nec >= 0:
            p = nec / total_elementos
            soma += p * math.log2(p)
    
    return -soma

# Exemplos de uso com impressão formatada
N1 = 0
N2 = 200
entropia = entropia(N1, N2)
print('{0:.2f}: entropia de um conjunto com {1} elementos de um tipo e {2} de outro tipo.'.format(entropia, N1, N2))

N1 = 200
N2 = 200
entropia = entropia(N1, N2)
print('{0:.2f}: entropia de um conjunto com {1} elementos de um tipo e {2} de outro tipo.'.format(entropia, N1, N2))

N1 = 20
N2 = 180
entropia = entropia(N1, N2)
print('{0:.2f}: entropia de um conjunto com {1} elementos de um tipo e {2} de outro tipo.'.format(entropia, N1, N2))

N1 = 180
N2 = 20
entropia = entropia(N1, N2)
print('{0:.2f}: entropia de um conjunto com {1} elementos de um tipo e {2} de outro tipo.'.format(entropia, N1, N2))
