from math import sqrt

limite = 1000000
L = [True for i in range(limite)]
L[0] = L[1] = False

i = 2
while i < int(sqrt(limite)) + 1:
    if L[i] == True:
        for multiple in range(i * i, limite, i):
            L[multiple] = False
    i += 1

Primes=[]
for i in range(limite):
    if L[i]:
        Primes.append(i)

def decomposition_facteurs_premiers_sans_multiplicite(n):
    if n <= 1:
        return []
    
    facteurs = []
    temp_n = n

    for p in Primes:
        if p * p > temp_n:
            break
            
        while temp_n % p == 0:
            facteurs.append(p) 
            temp_n //= p
            
    if temp_n > 1:
        facteurs.append(temp_n)
    P=set(facteurs)
    facteurs=list(P)

        
    return facteurs



L=[False for i in range(1000001)]
for i in range(2, 1000001):
    F=decomposition_facteurs_premiers_sans_multiplicite(i)
    if len(F)>3:
        L[i]=True
        c=0
        for e in range(i-3,i):
            if L[e]==True:
                c+=1
        if c==3:
            print(i-3)
            break
