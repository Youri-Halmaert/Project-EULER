def est_premier(n):
    """
    Vérifie si un nombre entier n est premier.
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    i = 3

    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def polynome(a, b, n):
    """
    Calcule n^2 + an + b
    """
    return n * n + a * n + b

L_primes = []
for i in range(2, 1001): 
    if est_premier(i):
        L_primes.append(i)

max_consecutive_primes = 0
result_product = 0


for b in L_primes:

    for a in range(-999, 1000): 
        n = 0

        while True:
            valeur = polynome(a, b, n)

            if valeur <= 0 or not est_premier(valeur):
                break
            n += 1

        consecutive_primes = n

        if consecutive_primes > max_consecutive_primes:
            max_consecutive_primes = consecutive_primes
            result_product = a * b
            

print(f"\nLe nombre maximum de premiers consécutifs trouvés est : {max_consecutive_primes}")
print(f"Le produit des coefficients (a * b) est : {result_product}")