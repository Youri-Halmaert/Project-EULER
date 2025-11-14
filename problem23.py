# ne trouverait on pas tous le nombre entiers qui peuvent 
# s'écrire comme la somme de deux nombres abondants?

# --> pour cela : on trouve d'abord tous les nombres abondants
# puis on fait la somme de deux nombres abondants et on marque (pour toutes les combinaisons)

def divisorsum(n):
    s=0
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            s+=i
            if i!=1 and i!=n//i:
                s+=n//i
    return s

#on trouve les nombres abondants plus petit que 28123
L=[]
for i in range(1,28124):
    if divisorsum(i)>i:
        L.append(i)


T=[False]*28124
for i in range(len(L)):
    for j in range(i,len(L)):
        if L[i]+L[j]<=28123:
            T[L[i]+L[j]]=True


S=0
for i in range(1,28124):
    if not T[i]:
        S+=i
print(S)