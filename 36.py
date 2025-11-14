def base2(n):
    L=[]
    L.append(n%2)
    while n>=1:
        n=n//2
        L.append(n%2)
    L.reverse()
    s=''
    for i in L:
        s=s+str(i)
    return int(s)

def is_palindrom(n):
    L=[str(n)[i] for i in range(len(str(n)))]
    T=L.copy()
    L.reverse()
    if L==T:
        return True

    else:
        return False

#print(is_palindrom(11211))

S=0
for i in range(1000000):
    if is_palindrom(i):
        b=base2(i)
        if is_palindrom(b):
            S+=i
print(S)