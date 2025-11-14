F=[1,1]
i=2
while len(str(F[-1]))<1000:
    F.append(F[i-1]+F[i-2])
    i+=1

print(len(F))
