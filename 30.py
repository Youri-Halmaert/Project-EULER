L=[]

#7*9**5 = 413 343 < 1 000 000 qui contient 7 chiffres donc on ne cherche pas de nombre a 7 chiffres ou plus
#on cherche entre 10 et 354 294 (= 6*9**5)

for n in range(10,354295):
    s=0
    for c in str(n):
        s+=int(c)**5
    if s==n:
        L.append(n)

print(sum(L))