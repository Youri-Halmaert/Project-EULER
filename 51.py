import math
from itertools import combinations

def crible_eratosthene(limite):
    est_premier = [True] * (limite + 1)
    est_premier[0] = est_premier[1] = False

    for nombre in range(2, int(math.sqrt(limite)) + 1):
        if est_premier[nombre]:
            for multiple in range(nombre * nombre, limite + 1, nombre):
                est_premier[multiple] = False

    liste_premiers = []
    for nombre in range(2, limite + 1):
        if est_premier[nombre]:
            liste_premiers.append(nombre)
            
    return liste_premiers

LIMITE = 1000000

premiers = crible_eratosthene(1000000)
#print(premiers)
S=set(premiers)

def search():
    for prime in premiers:
        str_prime = str(prime)
        L = len(str_prime)
        
        if L < 2:
            continue

        for num_replace in range(1, L): 
            limite_combinaison = L - 1 

            for indices in combinations(range(limite_combinaison), num_replace):
                
                chiffre_original = str_prime[indices[0]]
                
                if not all(str_prime[i] == chiffre_original for i in indices):
                    continue
                
                c = 0
                
                for d in range(10):
                    
                    if indices[0] == 0 and d == 0:
                        continue
                    
                    temp_list = list(str_prime)
                    
                    for index in indices:
                        temp_list[index] = str(d)
                    
                    nouveau_nombre = int("".join(temp_list))
                    
                    if nouveau_nombre in S and len(str(nouveau_nombre)) == L:
                        c += 1
                        print(nouveau_nombre)
                        
                if c >= 8:
                    return prime
                
    return 't es nul'


print(search())