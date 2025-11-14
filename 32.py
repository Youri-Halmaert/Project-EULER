sum=0
L=[]
for i in range(1,100):
    for j in range(10,10000):
        n=i*j
        s=str(n)+str(i)+str(j)
        if len(s)==9 and all(s.count(d)==1 for d in '123456789') and n not in L:
            sum+=n
            L.append(n)
            print(i,j,n)
print(sum)