max=0
for i in range(1,1001):
    count=0
    for a in range(1,min(i,333)):
        for b in range(a,min(i,501)):
            c=i-a-b
            if a**2+b**2==c**2:
                count+=1
    if count>max:
        max=count
        res=i

print(max)
print(res)
