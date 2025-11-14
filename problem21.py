L=[0*10000]

def divisorsum(n):
    s=0
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            s+=i
            if i!=1 and i!=n//i:
                s+=n//i
    return s

for i in range(1,10001):
    L.append(divisorsum(i))

S=0
for i in range(1,10001):
    j=L[i]
    if j<=10000 and L[j]==i and i!=j:
        S+=i

print(S)