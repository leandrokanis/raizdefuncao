'''
@author: leandrokanis
@note: Raiz de funcao usando o metodo de Bisseccao
'''

# funcao a ser trabalhada
def f(x):
    return x**4-4

a = 1.0 # limite inferior
b = 3.0 # limite superior
    
low     = a
high    = b
epsilon = 0.001
k       = 0

while True > epsilon:
    
    k += 1 # quantidade de iteracoes
    
    midpoint = (high+low)/2.0 # ponto medio
        
    if abs(f(midpoint)) < epsilon:
        break
    elif f(low)*f(midpoint) < 0:
        high = midpoint
    else:
        low = midpoint
        
    print k, midpoint, f(midpoint)

print k, midpoint, f(midpoint)