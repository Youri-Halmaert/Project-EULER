# 20 among 40
#The roads contains 2*n deplacements, n towards right and n towards down.
#The number of different roads is the number of different arrangements of these 2*n deplacements

def binomial_coefficient(n, k):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    k = min(k, n - k)  # Take advantage of symmetry
    c = 1
    for i in range(k):
        c = c * (n - i) // (i + 1)
    return c

print(binomial_coefficient(40, 20))


""""
def routes_dynamique(N: int) -> int:
    if N < 0:
        return 0
        
    # Initialise un tableau (une ligne de la grille) avec N+1 colonnes.
    # Tous les bords (première ligne) ont 1 route possible.
    grid = [1] * (N + 1)
    
    # Parcourt les lignes restantes (de 1 à N)
    for i in range(1, N + 1):
        # La première colonne de chaque ligne est toujours 1 (C(i, 0) = 1)
        grid[0] = 1 
        
        # Parcourt les colonnes restantes (de 1 à N) et applique la récurrence
        # grid[j] (nouveau) = grid[j] (ancien, C(i-1, j)) + grid[j-1] (nouveau, C(i, j-1))
        for j in range(1, N + 1):
            grid[j] = grid[j] + grid[j-1]
            
    # Le résultat final est dans la dernière cellule calculée (C(N, N))
    return grid[N]

# Exemple d'utilisation pour la grille 20 x 20
N = 20
resultat_dynamique = routes_dynamique(N)
print(f"Le nombre de routes pour une grille {N}x{N} est : {resultat_dynamique}")
"""