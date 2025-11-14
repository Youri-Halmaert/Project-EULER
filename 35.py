from math import sqrt

limite = 1000000
L = [True for i in range(limite)]
L[0] = L[1] = False

i = 2
while i < int(sqrt(limite)) + 1:
    if L[i] == True:
        for multiple in range(i * i, limite, i):
            L[multiple] = False
    i += 1

count = 0
for i in range(limite):
    if L[i]:
        s_num = str(i)
        is_circular = True
        
        for j in range(len(s_num)):
            rotated_str = s_num[j:] + s_num[:j]
            rotated_int = int(rotated_str)
            
            if L[rotated_int] == False:
                is_circular = False
                break
        
        if is_circular:
            count += 1

print(count)