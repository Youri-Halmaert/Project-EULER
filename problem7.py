def est_premier(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n=0
N=10001
while N>0:
    n+=1
    if est_premier(n):
        N-=1
print(n)