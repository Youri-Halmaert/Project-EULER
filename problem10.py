'''def est_premier(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
s=0
for i in range(2, 2000000):
    if est_premier(i):
        s+=i
print(s)'''

def sum_primes_below(limit):
    """
    Calculates the sum of all primes below 'limit' using the
    Sieve of Eratosthenes.
    """
    
    sieve = [True] * limit
    
    sieve[0] = False
    sieve[1] = False
    

    for p in range(2, int(limit**0.5) + 1):
        if sieve[p]:
            for i in range(p * p, limit, p):
                sieve[i] = False
                
    total_sum = 0
    for number, is_prime in enumerate(sieve):
        if is_prime:
            total_sum += number
            
    return total_sum



total = sum_primes_below(2000000)
print(total)