import itertools
import math

def is_prime(nombre):
    if nombre <= 1:
        return False
    if nombre <= 3:
        return True

    if nombre % 2 == 0 or nombre % 3 == 0:
        return False
        
    i = 5
    limite = int(math.sqrt(nombre))
    
    while i <= limite:
        if nombre % i == 0 or nombre % (i + 2) == 0:
            return False
        i += 6
        
    return True

def prime_pan():
    for n in range(7, 0, -1):
        chiffres = [str(i) for i in range(1, n + 1)]
        chiffres.sort(reverse=True)
        
        compteur_tests = 0
        
        for p in itertools.permutations(chiffres):
            nombre_str = "".join(p)
            nombre = int(nombre_str)
            compteur_tests += 1
            
            if is_prime(nombre):
                return nombre 

        
print(prime_pan())