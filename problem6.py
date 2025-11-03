def sum_square_diff(n):
    S=(n*(n+1)/2)**2
    S2=sum(i**2 for i in range(1,n+1))
    return S-S2

print(int(sum_square_diff(100)))