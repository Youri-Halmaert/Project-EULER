from math import sqrt

limite = 9999
L = [True for i in range(limite)]
L[0] = L[1] = False

i = 2
while i < int(sqrt(limite)) + 1:
    if L[i] == True:
        for multiple in range(i * i, limite, i):
            L[multiple] = False
    i += 1

P=[]
for i in range(9999):
    if L[i]:
        P.append(i)
Primes=set(P)

for i in range(len(P)):
    for j in range(i+1,len(P)):
        if (P[j]-P[i])*2+P[i] in Primes:
            if sorted(str(P[i]))==sorted(str(P[j]))==sorted(str((P[j]-P[i])*2+P[i])):
                print(P[i], P[j],(P[j]-P[i])*2+P[i])
