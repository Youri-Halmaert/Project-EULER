current=2 #first day of 1901 is a tuesday
sunday_count = 0
DAYS_PER_MONTH = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # Index 1-12


for i in range(1901,2001):
    leap=False
    if i%4==0:
        leap=True
    if i%100==0 and  i%400==0:
        leap=False


    for month in range(1, 13):
        if current==0:
            sunday_count+=1

        days_in_month = DAYS_PER_MONTH[month]
        if month == 2 and leap:
            days_in_month = 29
        current = (current + days_in_month) % 7

print(sunday_count)
