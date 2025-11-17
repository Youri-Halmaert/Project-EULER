import random
from random import randint

Blue=[(random.randint(0,255), random.randint(0,255)),(random.randint(0,255), random.randint(0,255))]
Red=[(random.randint(0,255), random.randint(0,255)),(random.randint(0,255), random.randint(0,255)),(random.randint(0,255), random.randint(0,255))]
D=[]

def intersection(A, B, C, D):
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C
    x4, y4 = D

    den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

    if den == 0:
        print("probleme : droites parallèles ou confondues")
        return None 

    t = (x1*y2 - y1*x2)
    u = (x3*y4 - y3*x4)

    x = (t * (x3 - x4) - (x1 - x2) * u) / den
    y = (t * (y3 - y4) - (y1 - y2) * u) / den

    return (x, y)


for day in range(16):
    #
