#53 est le premier nb premier plus grand que 47 (qui est le dernier acceptable dcp)
L=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]

def decompose_en_facteurs_premiers(n, primes_list):
    if n < 2:
        return []
    facteurs = []

    # === Étape 1 : Utiliser la liste pré-calculée ===
    
    for p in primes_list:
        # Optimisation : Si p*p > n, alors n (s'il est > 1) 
        # doit être le dernier facteur premier.
        if p * p > n:
            break
        
        # Diviser par p autant de fois que possible
        while n % p == 0:
            facteurs.append(p)
            n = n // p
    
    # Si on a fini, on retourne le résultat
    if n == 1:
        return facteurs

    # === Étape 2 : La liste n'était pas suffisante, continuer ===
    
    # Déterminer par où commencer la suite de la division.
    # Si la liste était vide, on commence à 2.
    if not primes_list:
        d = 2
    else:
        # On commence au nombre suivant le plus grand prime de la liste
        d = primes_list[-1] + 1

    # Cas spécial : Si on doit commencer par 2 (liste vide)
    if d == 2:
        while n % 2 == 0:
            facteurs.append(2)
            n = n // 2
        d = 3 # On passe aux nombres impairs

    # Si le nombre suivant (d) est pair (ex: liste finissait à 3, d=4),
    # on le passe à impair (ex: d=5).
    if d > 2 and d % 2 == 0:
        d += 1
        
    # === Étape 3 : Division successive standard (optimisée) ===
    
    # Continuer la division par les nombres impairs (d, d+2, d+4...)
    while d * d <= n:
        while n % d == 0:
            facteurs.append(d)
            n = n // d
        d += 2
        
    # Si n est toujours supérieur à 1 après la boucle,
    # c'est que n lui-même est le dernier facteur premier.
    if n > 1:
        facteurs.append(n)
        
    return facteurs

def verifier_plus_petit_facteur(n, primes_list):
    """
    Vérifie si le plus petit facteur premier de n est 47 ou moins.
    
    Retourne True si le plus petit facteur premier est <= 47.
    Retourne False sinon (y compris si n < 2).
    """
    
    # Gérer les cas de base (0, 1, négatifs) qui n'ont pas
    # de facteurs premiers.
    if n < 2:
        return False
        
    # 1. Obtenir la liste complète des facteurs
    facteurs = decompose_en_facteurs_premiers(n, primes_list)
    
    # 2. Si la liste est vide (ne devrait pas arriver si n >= 2,
    #    mais par sécurité)
    if not facteurs:
        return False
        
    # 3. Le plus grand facteur est le premier de la liste
    plus_grand_facteur = facteurs[-1]
    
    # 4. Renvoyer la comparaison
    return plus_grand_facteur <= 47


def T(n):
    return n*(n+1)//2
print(T())
#print(decompose_en_facteurs_premiers(T(53),L))

print(verifier_plus_petit_facteur(T(),L))

def is_p_smooth(p, n):
    """dit si T(n) est p-smooth (indice n)"""


