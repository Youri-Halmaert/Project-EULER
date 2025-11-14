L=[]
for i in range(10,100):
    for j in range(10,100):
        if i/j==int(str(i)[0])/int(str(j)[0]) and str(i)[1]==str(j)[1] and  str(j)[0]!='0' and i!=j and (i,j) not in L:
            L.append((i,j))
        if i/j==int(str(i)[1])/int(str(j)[0]) and str(i)[0]==str(j)[1] and  str(j)[0]!='0' and i!=j and (i,j) not in L:
            L.append((i,j))
        if str(i)[1]==str(j)[0] and  str(j)[1]!='0' and i!=j and i/j==int(str(i)[0])/int(str(j)[1]) and (i,j) not in L:
            L.append((i,j))
        if str(i)[0]==str(j)[0] and  str(j)[1]!='0' and i!=j and i/j==int(str(i)[1])/int(str(j)[1]) and (i,j) not in L:
            L.append((i,j))
print(L)
# 19/95 49/98 16/64 26/65
print(19/95 *49/98 *16/64 *26/65)