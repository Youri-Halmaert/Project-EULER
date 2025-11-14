def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)
    
#nb permutations = n!
#print(fact(10))
#print(fact(9))
T=[0,1,2,3,4,5,6,7,8,9]
N=999999
for i in range(10):
    a= N//fact(9-i)
    if a>0:
        N-=a*fact(9-i)
    print(T[a])
    T.pop(a)


print(2*fact(9)+6*fact(8)+6*fact(7)+2*fact(6)+5*fact(5)+fact(4)+2*fact(3)+2*fact(2)+0*fact(1))

