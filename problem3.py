def est_premier(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def premiers_nombres(n):
    primes = []
    num = 2
    while len(primes) < n:
        if est_premier(num):
            primes.append(num)
        num += 1
    return primes

# Générer les 500 premiers nombres premiers
premiers_500 = premiers_nombres(1500)
print(premiers_500)

n=600851475143
m=0
while n>1:
    for p in premiers_500:
        if n%p==0:
            n=n//p
            m=p
            break
print(m)