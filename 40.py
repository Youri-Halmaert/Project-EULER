L=[]
for i in range(300000):
    i=str(i)
    for j in range(len(i)):
        L.append(i[j])

sum=int(L[1])*int(L[10])*int(L[100])*int(L[1000])*int(L[10000])*int(L[100000])*int(L[1000000])
print(sum)