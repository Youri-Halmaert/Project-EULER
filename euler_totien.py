def calculer_totient_euler_crible(N):
    """
    Calcule la fonction totient d'Euler (phi) pour tous les nombres
    de 1 à N en utilisant une méthode de crible (crible du totient).
    Complexité : O(N log log N)

    Args:
        N (int): La limite supérieure (jusqu'à 1,000,000 dans ce cas).

    Returns:
        list: Une liste où liste_phi[i] est la valeur de phi(i).
    """
    # 1. Initialisation : phi[i] = i
    # Nous avons besoin d'une taille N+1 pour indexer jusqu'à N.
    liste_phi = list(range(N + 1))
    
    # phi(1) est 1 par définition
    liste_phi[1] = 1

    # 2. Parcours des nombres de 2 à N
    for i in range(2, N + 1):
        
        # Si liste_phi[i] == i, cela signifie que i n'a pas encore été mis 
        # à jour par un facteur premier plus petit. Donc, i est un NOMBRE PREMIER.
        if liste_phi[i] == i:
            
            # Pour un nombre premier p, phi(p) = p - 1.
            liste_phi[i] = i - 1
            
            # 3. Mise à jour des multiples de ce nombre premier i
            # On commence par le premier multiple > i (2*i)
            # On parcourt j = 2*i, 3*i, 4*i, ... jusqu'à N
            for j in range(2 * i, N + 1, i):
                
                # Appliquer la propriété : pour tout multiple j de i,
                # on utilise la contribution du facteur premier i : (1 - 1/i)
                # qui est équivalent à multiplier par (i - 1) / i.
                # Cela se traduit par : phi[j] = phi[j] * (i - 1) // i
                liste_phi[j] = liste_phi[j] // i * (i - 1) 
                
    return liste_phi

L=calculer_totient_euler_crible(1000000)
max=1
n=1
for i in range(2,len(L)):
    if i/L[i]>max:
        max=i/L[i]
        n=i

print(n)