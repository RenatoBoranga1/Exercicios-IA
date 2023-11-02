import math

def entropia(p1, p2):
   
    if not (0 <= p1 <= 1) or not (0 <= p2 <= 1) or not math.isclose(p1 + p2, 1):
        raise ValueError("As proporções p1 e p2 devem somar 1 e estar no intervalo [0, 1].")

    if p1 == 0 or p2 == 0:
        return 0.0 
    else:
        return -p1 * math.log2(p1) - p2 * math.log2(p2)


print(entropia(0, 1))  
print(entropia(0.5, 0.5)) 
print(entropia(0.1, 0.9))  
print(entropia(0.9, 0.1))  