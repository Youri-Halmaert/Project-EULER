import time

def find_longest_collatz(limit):

    
    # Le dictionnaire stocke {nombre: longueur_de_la_chaine_partant_de_ce_nombre}
    cache = {1: 1}  # Cas de base : la chaîne commençant à 1 a une longueur de 1.
    
    longest_chain = 0
    starting_number = 0

    # On teste tous les nombres de 2 à la limite
    for start in range(2, limit):
        
        n = start
        path = []  # Pour stocker les nombres non encore vus

        # 1. Suivre la chaîne jusqu'à trouver un nombre déjà dans le cache
        while n not in cache:
            path.append(n)
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3 * n + 1
        
        # 2. On a trouvé un nombre 'n' dont on connaît la longueur (cache[n])
        # On va maintenant "remonter" le chemin (path) et remplir le cache
        
        # 'current_len' commence à la longueur du premier nombre connu
        current_len = cache[n]
        
        for num in reversed(path):
            # Chaque étape en arrière ajoute 1 à la longueur
            current_len += 1
            cache[num] = current_len

        # 3. Vérifier si ce nombre de départ (start) est le nouveau record
        # Note : cache[start] a été défini lors de la dernière itération de la
        # boucle "reversed(path)"
        
        if cache[start] > longest_chain:
            longest_chain = cache[start]
            starting_number = start
            
    return starting_number, longest_chain

# --- Exécution ---
LIMIT = 1_000_000
start_time = time.time()

num, length = find_longest_collatz(LIMIT)
end_time = time.time()

print(f"Calcul terminé en {end_time - start_time:.4f} secondes.")
print("---")
print(f"Le nombre de départ < {LIMIT} produisant la plus longue chaîne est : {num}")
print(f"Longueur de la chaîne : {length}")