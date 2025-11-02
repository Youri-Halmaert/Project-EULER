'''
Find the sum of the squares of all odd numbers from 1 to 235,000.
'''
sum=0
for i in range (1,235001):
    if i%2==1:
        sum+=i**2
print(sum)
