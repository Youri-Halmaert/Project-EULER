# (a+b)^2=(1000-c)^2
# 2ab=1000^2-2*1000c
# 
# ab +1000c=500000
# a+b+c =1000

for a in range(1, 333):
    for b in range(a + 1, 500):
        c = 1000 - a - b
        if a * b == 500000 - 1000 * c:
            print(f"Triplet trouvé : a={a}, b={b}, c={c}")
            print(a * b * c)
            break

'''def solve_triplet_by_sum(s):

    for a in range(3, s // 3):
        for b in range(a + 1, (s - a) // 2):
            c = s - a - b
            if a*a + b*b == c*c:
                # output (a,b,c)
                print(f"Triplet trouvé : a={a}, b={b}, c={c}")
                print(f"Vérification somme : {a} + {b} + {c} = {a+b+c}")
                return a * b * c
    return None

# --- Exécution ---
somme_voulue = 1000
produit = solve_triplet_by_sum(somme_voulue)

if produit:
    print(f"\nLe produit a*b*c est : {produit}")
else:
    print(f"\nAucune solution trouvée pour s={somme_voulue}.")'''
