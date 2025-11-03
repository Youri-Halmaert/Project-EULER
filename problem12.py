'''def has_divisors(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count+=1
    return count


s=0
i=0
while True:
    if has_divisors(s)>500:
        break
    i+=1
    s+=i
print(s)'''

import time

def count_divisors(n):
    if n == 1:
        return 1
    
    total_divisors = 1
    
    # Gérer le facteur 2
    count = 0
    while n % 2 == 0:
        count += 1
        n //= 2
    total_divisors *= (count + 1)
    
    # Gérer les facteurs impairs
    d = 3
    while d * d <= n:
        count = 0
        while n % d == 0:
            count += 1
            n //= d
        total_divisors *= (count + 1)
        d += 2
        
    # Si n est encore > 1, c'est un facteur premier
    if n > 1:
        total_divisors *= 2
        
    return total_divisors

def find_triangle_with_divisors(target_divisors):
    n = 1
    num_divisors = 0
    
    while num_divisors <= target_divisors:
        n += 1
        
        # Nous devons trouver d(n/2) * d(n+1) ou d(n) * d((n+1)/2)
        
        if n % 2 == 0:
            # Cas 1: n est pair. T_n = (n/2) * (n+1)
            div1 = count_divisors(n // 2)
            div2 = count_divisors(n + 1)
        else:
            # Cas 2: n est impair. T_n = n * ((n+1)/2)
            div1 = count_divisors(n)
            div2 = count_divisors((n + 1) // 2)
            
        num_divisors = div1 * div2
        
    # L'indice est n. Le nombre triangulaire est n*(n+1)/2
    triangle_number = n * (n + 1) // 2
    return triangle_number, num_divisors, n

# --- Exécution ---
start_time = time.time()
target = 500

result_number, div_count, index_n = find_triangle_with_divisors(target)
end_time = time.time()

print(f"Objectif : Trouver le premier nombre triangulaire avec > {target} diviseurs.")
print("---")
print(f"Résultat : {result_number}")
print(f"Indice (n) : {index_n} (c'est le {index_n}e nombre triangulaire)")
print(f"Nombre de diviseurs : {div_count}")
print(f"Temps de calcul : {end_time - start_time:.4f} secondes")