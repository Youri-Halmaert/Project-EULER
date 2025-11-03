def is_palindrome(n):
    """Vérifie si un nombre est un palindrome."""
    # Convertit le nombre en chaîne de caractères
    s = str(n)
    # Compare la chaîne avec son inverse
    return s == s[::-1]

def find_largest_palindrome_product():
    """
    Trouve le plus grand palindrome formé par le produit de deux nombres à 3 chiffres.
    Inclut l'optimisation pour un arrêt précoce.
    """
    largest_palindrome = 0
    
    # 1. Parcourir les facteurs i et j de 999 à 100
    # On commence par les plus grands nombres, car le plus grand produit est au début.
    for i in range(999, 99, -1):
        
        # Optimisation : Si le produit maximum possible pour le facteur i
        # (c'est-à-dire i * 999) est déjà inférieur au plus grand palindrome trouvé,
        # il est inutile de continuer avec des facteurs i plus petits.
        if i * 999 <= largest_palindrome:
            break
            
        # Parcourir j à partir de i (car i * j = j * i, on évite les doublons)
        for j in range(i, 99, -1):
            product = i * j
            
            # Optimisation : Si le produit actuel est déjà plus petit ou égal
            # au plus grand palindrome trouvé, on passe au i suivant.
            # (Pour ce j et tous les j suivants, le produit sera encore plus petit.)
            if product <= largest_palindrome:
                break
                
            # 2. Vérifier si le produit est un palindrome
            if is_palindrome(product):
                # 3. Conserver le plus grand palindrome
                largest_palindrome = product
                # Inutile de continuer la boucle j, car tous les j suivants donneront un produit plus petit.
                break 

    return largest_palindrome

# Exécution
resultat = find_largest_palindrome_product()
print(f"Le plus grand palindrome fait du produit de deux nombres à 3 chiffres est : {resultat}")