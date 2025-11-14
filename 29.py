L=[]
for a in range(2,101):
    for b in range(2,101):
        L.append(a**b)
L=list(set(L))
print(len(L))
