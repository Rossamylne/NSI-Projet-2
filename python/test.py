'''

# On commence par définir les valeurs des pièces de monnaie que nous allons utiliser
coin_values = [1, 5, 10, 25]

# On demande à l'utilisateur d'entrer la somme à payer
total_due = float(input("Entrez le montant total à payer : "))

# On demande à l'utilisateur d'entrer la somme qu'il a donnée
amount_paid = float(input("Entrez le montant que vous avez donné : "))

# On calcule la différence entre la somme due et la somme payée
change_due = round(amount_paid - total_due, 2)

# On initialise un compteur pour compter le nombre de pièces à rendre
num_coins = 0

# On utilise une boucle pour parcourir les différentes valeurs de pièces de monnaie
for value in coin_values:
    # On calcule le nombre de pièces de chaque valeur à rendre
    num_coins += change_due // value
    # On met à jour la somme à rendre en enlevant la valeur des pièces rendues
    change_due = round(change_due % value, 2)

# On affiche le nombre total de pièces à rendre
print("Vous devez rendre un total de " + str(num_coins) + " pièces.")

'''


def monnaie_a_rendre(argent):
    '''
    Fonction qui donne la monnaie à rendre en fonction d'un montant donné.
    A l'aide d'une liste qui contient les différentes monnaie qu'on puisse rendre,
    on parcours cette liste 
    '''
    monnaies = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    while argent > 0:
        for monnaie in monnaies:
            if monnaie <= argent:
                argent -= monnaie
                print(f'Il faut rendre {monnaie} euros')
                break

monnaie_a_rendre(595)

