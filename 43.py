import itertools as it

def p():

    D = [2, 3, 5, 7, 11, 13, 17]
    S = []
    for P in it.permutations('0123456789'):
        if P[0] == '0':
            continue

        v = True
        for j in range(1, 8):
            s = int(P[j] + P[j+1] + P[j+2])
            
            if s % D[j-1] != 0:
                v = False
                break
        
        if v:
            S.append(int("".join(P)))
            
    return sum(S)

r = p()
print(r)