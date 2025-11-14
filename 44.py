L=[]
for i in range(1,5000):
    L.append(int(i*(3*i-1)/2))
S=set(L)
max=99999999999999999999
for e in range(len(L)):
    for r in range(e+1,len(L)):
        if L[e]+L[r] in S:
            if L[r]-L[e] in S and L[r]-L[e]<max :
                max=L[r]-L[e]
                res=(L[r],L[e])

print(max)
print(res)