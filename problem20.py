L=[1]
for i in range(1,100):
    L.append((i+1)*L[i-1])

print(L)
print(len(L))
S=str(L[99])
sum=0
for i in S:
    sum+=int(i)
print(sum)