def trouver_cycle(n):
    seen = {}
    value = 1
    position = 0

    while True:
        if value == 0:
            return 0  # Terminating decimal, no cycle
        if value in seen:
            return position - seen[value]  # Length of the cycle
        seen[value] = position
        value = (value * 10) % n
        position += 1

max=0
for i in range(1,1000):
    if max<trouver_cycle(i):
        max=trouver_cycle(i)
        res=i
print(res)