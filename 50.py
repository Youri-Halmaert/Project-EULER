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

P=set(Primes)

max=0
count=0
for i in range(len(Primes)):
    c=0
    count=0
    for j in range(i, len(Primes)):
        if count>=limite:
            break
        count+=Primes[j]
        c+=1
        if c>max and count in P:
            max=c
            sum= count


print(sum)