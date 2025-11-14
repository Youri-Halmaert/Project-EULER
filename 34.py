import itertools


#(fact(9)) #362880

#(8*fact(9)) #2 903 040
# we conclude that a 8 digit number cant be written as the sum the factorial of their digits
#so we go until at 7*fact(9) = 2540160


FACTORIALS = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

found_numbers = set()

digits = range(10)

for n in range(2, 8):
    for combo in itertools.combinations_with_replacement(digits, n):
        
        sum_of_facts = sum(FACTORIALS[d] for d in combo)
        
        s_sum = str(sum_of_facts)
        
        if len(s_sum) != n:
            continue
        
        sum_digits_sorted = sorted(int(d) for d in s_sum)
        combo_sorted = sorted(combo)
        
        if sum_digits_sorted == combo_sorted and sum_of_facts > 9:
            found_numbers.add(sum_of_facts)

print(sum(found_numbers))