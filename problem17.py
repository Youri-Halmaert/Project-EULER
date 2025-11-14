D = {
    '0': 'zero',
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine',
}

def decomp(n):
    if n == 1000:
        print("one thousand")
        return(11)
    
    h = n // 100
    d = (n % 100) // 10
    u = n % 10
    number = ""
    
    if str(h) != '0':
        # Correction de l'erreur : D[clé] au lieu de D.value(clé)
        number = D[str(h)] + " hundred"
        if d != 0 or u != 0:
            number = number + " and "
            
    if d == 1:
        if u == 0:
            number = number + "ten"
        elif u == 1:
            number = number + "eleven"
        elif u == 2:
            number = number + "twelve"
        elif u == 3:
            number = number + "thirteen"
        elif u == 4:
            number = number + "fourteen"
        elif u == 5:
            number = number + "fifteen"
        elif u == 6:
            number = number + "sixteen"
        elif u == 7:
            number = number + "seventeen"
        elif u == 8:
            number = number + "eighteen"
        elif u == 9:
            number = number + "nineteen"
    else:
        if d == 2:
            number = number + "twenty"
        elif d == 3:
            number = number + "thirty"
        elif d == 4:
            number = number + "forty"
        elif d == 5:
            number = number + "fifty"
        elif d == 6:
            number = number + "sixty"
        elif d == 7:
            number = number + "seventy"
        elif d == 8:
            number = number + "eighty"
        elif d == 9:
            number = number + "ninety"
        
        if u != 0 and d != 0:
            number = number + "-"
        
        if u != 0:
            # Correction de l'erreur : D[clé] au lieu de D.value(clé)
            number = number + D[str(u)]
    
    return(len(number.replace(" ", "").replace("-", "")))

print(sum(decomp(i) for i in range(1, 1001)))