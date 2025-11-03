"""
Problem 84

A player starts on the GO square and adds the scores on two 6-sided dice to determine 
the number of squares they advance in a clockwise direction. Without any further rules 
we would expect to visit each square with equal probability: 2.5%. However, landing 
on G2J (Go To Jail), CC (community chest), and CH (chance) changes this distribution.

In addition to G2J, and one card from each of CC and CH, that orders the player to 
go directly to jail, if a player rolls three consecutive doubles, they do not advance 
the result of their 3rd roll. Instead they proceed directly to jail.

At the beginning of the game, the CC and CH cards are shuffled. When a player 
lands on CC or CH they take a card from the top of the respective pile and, after 
following the instructions, it is returned to the bottom of the pile. There are 
sixteen cards in each pile, but for the purpose of this problem we are only concerned
with cards that order a movement; any instruction not concerned with movement 
will be ignored and the player will remain on the CC/CH square.

Community Chest (2/16 cards):
Advance to GO
Go to JAIL
Chance (10/16 cards):
Advance to GO
Go to JAIL
Go to C1
Go to E3
Go to H2
Go to R1
Go to next R (railway company)
Go to next R
Go to next U (utility company)
Go back 3 squares.
The heart of this problem concerns the likelihood of visiting a particular square. 
That is, the probability of finishing at that square after a roll. For this reason 
it should be clear that, with the exception of G2J for which the probability of 
finishing on it is zero, the CH squares will have the lowest probabilities, as 
5/8 request a movement to another square, and it is the final square that the 
player finishes at on each roll that we are interested in. We shall make no 
distinction between "Just Visiting" and being sent to JAIL, and we shall also 
ignore the rule about requiring a double to "get out of jail", assuming that 
they pay to get out on their next turn.

By starting at GO and numbering the squares sequentially from 00 to 39 we can 
concatenate these two-digit numbers to produce strings that correspond with 
sets of squares.

Statistically it can be shown that the three most popular squares, in order, 
are JAIL (6.24%) = Square 10, E3 (3.18%) = Square 24, and GO (3.09%) = Square 00. 
So these three most popular squares can be listed with the six-digit 
modal string: 102400.

If, instead of using two 6-sided dice, two 4-sided dice are used, 
find the six-digit modal string.


"""





import numpy as np

def solve_monopoly_2d4():
    """
    Calcule la chaîne modale à six chiffres pour le Monopoly 
    en utilisant deux dés à 4 faces.
    """

    # --- 1. Définition des constantes du plateau ---
    
    # Positions des cases spéciales
    GO = 0
    JAIL = 10
    G2J = 30
    C1 = 11
    E3 = 24
    H2 = 39
    R1 = 5
    R2 = 15
    R3 = 25
    R4 = 35
    U1 = 12
    U2 = 28

    CC = [2, 17, 33]  # Community Chest
    CH = [7, 22, 36]  # Chance
    
    # Mappages pour les cartes "Aller au prochain R (chemin de fer) / U (service public)"
    # Clé = case Chance, Valeur = destination
    R_NEXT = {7: R2, 22: R3, 36: R1}
    U_NEXT = {7: U1, 22: U2, 36: U1}

    # --- 2. Probabilités des dés (2d4) ---
    
    # Il y a 4x4 = 16 résultats possibles
    P_DOUBLE = 4 / 16  # (1,1), (2,2), (3,3), (4,4)
    
    # Probabilités pour les lancers qui ne sont PAS des doubles
    # Somme 3: (1,2), (2,1) -> 2/16
    # Somme 4: (1,3), (3,1) -> 2/16
    # Somme 5: (1,4), (4,1), (2,3), (3,2) -> 4/16
    # Somme 6: (2,4), (4,2) -> 2/16
    # Somme 7: (3,4), (4,3) -> 2/16
    # Total = 12/16
    ROLL_PROBS = {
        3: 2/16,
        4: 2/16,
        5: 4/16,
        6: 2/16,
        7: 2/16
    }
    
    # Probabilités pour les lancers qui SONT des doubles
    # Somme 2: (1,1) -> 1/16
    # Somme 4: (2,2) -> 1/16
    # Somme 6: (3,3) -> 1/16
    # Somme 8: (4,4) -> 1/16
    # Total = 4/16
    DOUBLE_PROBS = {
        2: 1/16,
        4: 1/16,
        6: 1/16,
        8: 1/16
    }

    # --- 3. Fonction de gestion des atterrissages (G2J, CC, CH) ---

    def get_final_destinations(square):
        """
        Calcule la distribution de probabilité des cases finales
        après avoir atterri sur 'square'.
        Prend en compte G2J, CC, et CH (y compris les mouvements en chaîne).
        Retourne un tableau numpy de 40 éléments.
        """
        probs = np.zeros(40)
        
        if square == G2J:
            probs[JAIL] = 1.0
            
        elif square in CC:
            # 2 cartes de mouvement sur 16
            probs[square] = 14 / 16  # Reste sur la case
            probs[GO] = 1 / 16
            probs[JAIL] = 1 / 16
            
        elif square in CH:
            # 10 cartes de mouvement sur 16
            probs[square] = 6 / 16  # Reste sur la case
            probs[GO] += 1 / 16
            probs[JAIL] += 1 / 16
            probs[C1] += 1 / 16
            probs[E3] += 1 / 16
            probs[H2] += 1 / 16
            probs[R1] += 1 / 16
            probs[R_NEXT[square]] += 2 / 16  # 2 cartes "Prochain R"
            probs[U_NEXT[square]] += 1 / 16  # 1 carte "Prochain U"
            
            # Carte "Reculez de 3 cases" (1/16)
            back_3 = square - 3
            if back_3 == CC[2]:  # Atterrit sur CC3 depuis CH3
                # Mouvement en chaîne : 1/16 (Chance) * (Probas de CC)
                probs[GO] += (1/16) * (1/16)
                probs[JAIL] += (1/16) * (1/16)
                probs[CC[2]] += (1/16) * (14/16)
            else:
                probs[back_3] += 1/16
                
        else:
            # Case normale
            probs[square] = 1.0
            
        return probs

    # --- 4. Construction de la matrice de transition (120x120) ---
    
    # Un état est (case, nombre_de_doubles)
    # L'état k = case * 3 + nombre_de_doubles
    T = np.zeros((120, 120))

    for i in range(120):
        current_square = i // 3
        doubles_count = i % 3

        # A. Gérer les lancers NON-DOUBLES (réinitialise doubles_count à 0)
        next_doubles_count = 0
        for roll, prob in ROLL_PROBS.items():
            land_square = (current_square + roll) % 40
            final_probs = get_final_destinations(land_square)
            
            for final_square in range(40):
                if final_probs[final_square] > 0:
                    j = final_square * 3 + next_doubles_count
                    T[i, j] += prob * final_probs[final_square]

        # B. Gérer les lancers DOUBLES
        if doubles_count == 2:
            # Cas 1: 3ème double -> VA EN PRISON
            next_square = JAIL
            next_doubles_count = 0
            j = next_square * 3 + next_doubles_count
            T[i, j] += P_DOUBLE  # 4/16 (n'importe quel double)
        else:
            # Cas 2: 1er ou 2ème double
            next_doubles_count = doubles_count + 1
            for roll, prob in DOUBLE_PROBS.items():
                land_square = (current_square + roll) % 40
                final_probs = get_final_destinations(land_square)
                
                for final_square in range(40):
                    if final_probs[final_square] > 0:
                        j = final_square * 3 + next_doubles_count
                        T[i, j] += prob * final_probs[final_square]

    # --- 5. Calcul de la distribution stationnaire ---
    
    # Nous devons trouver le vecteur propre v tel que v * T = v
    # Ce qui est équivalent à T.T * v.T = v.T (où .T est la transposée)
    # Nous cherchons le vecteur propre de T.T pour la valeur propre 1.
    
    eig_vals, eig_vecs = np.linalg.eig(T.T)
    
    # Trouver le vecteur propre pour la valeur propre la plus proche de 1
    stationary_vec = eig_vecs[:, np.isclose(eig_vals, 1)].real
    
    # Normaliser le vecteur pour que la somme soit 1
    stationary_vec_120 = stationary_vec / stationary_vec.sum()
    
    # --- 6. Agréger les probabilités par case ---
    
    # Sommer les probabilités pour les 3 états de doubles (0, 1, 2)
    square_probs = np.zeros(40)
    for s in range(40):
        square_probs[s] = stationary_vec_120[s * 3] + \
                          stationary_vec_120[s * 3 + 1] + \
                          stationary_vec_120[s * 3 + 2]

    # --- 7. Trouver les 3 premiers et formater la sortie ---
    
    # Obtenir les indices des probabilités triées par ordre décroissant
    top_3_indices = np.argsort(square_probs)[::-1][:3]
    
    # Formater la chaîne modale
    modal_string = "".join(f"{idx:02d}" for idx in top_3_indices)
    
    return modal_string, square_probs, top_3_indices


if __name__ == "__main__":
    modal_string, probs, indices = solve_monopoly_2d4()
    
    print(f"La chaîne modale à six chiffres pour 2d4 est : {modal_string}\n")
    print("Top 3 des cases les plus visitées :")
    for i, idx in enumerate(indices):
        print(f"  {i+1}. Case {idx:02d} (Probabilité : {probs[idx]:.4%})")

for i in range(40):
        print(f"Case {i:02d}: {probs[i]:.4%}")
