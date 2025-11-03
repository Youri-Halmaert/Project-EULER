#1. on decompose les nombres en produits de facteurs premiers
#2. on regarde dans T si ce nombre premier est présent, ainsi que sa multiplicité, sinon on ajoute

import math

def decomposition_facteurs_premiers(n):
    """
    Décompose un entier n > 1 en un dictionnaire de ses facteurs premiers,
    où les clés sont les bases premières et les valeurs sont leurs exposants.
    """
    
    facteurs = {}
    
    if n <= 1:
        return facteurs  # Retourne un dictionnaire vide pour 0, 1 ou négatifs

    # --- 1. Gérer le facteur 2 ---
    exposant = 0
    while n % 2 == 0:
        exposant += 1
        n = n // 2
    
    if exposant > 0:
        facteurs[2] = exposant
        
    # --- 2. Gérer les facteurs impairs (à partir de 3) ---
    limite = int(math.sqrt(n)) + 1
    
    for d in range(3, limite, 2):
        if n == 1:
            break
            
        exposant = 0
        while n % d == 0:
            exposant += 1
            n = n // d
        
        if exposant > 0:
            facteurs[d] = exposant
            
    # --- 3. Gérer le cas final (si n est un premier > 1) ---
    if n > 1:
        facteurs[n] = 1
        
    return facteurs



L=[i for i in range(1,21)]

T={}


n=1
for i in L:
    a=decomposition_facteurs_premiers(i)
    for p in a:
        if p in T:
            T[p]=max(T[p],a[p])
        else:
            T[p]=a[p]

for p in T:
    n=n*(p**T[p])
print(T)
print(n)