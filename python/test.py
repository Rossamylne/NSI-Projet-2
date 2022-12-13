def monnaie_a_rendre(argent):
    '''
    Fonction qui donne la monnaie à rendre en fonction d'un montant donné.
    A l'aide d'une liste qui contient les différentes monnaie qu'on puisse rendre,
    on parcours cette liste et on regarde si la valeur séléctionnée peut être déduite
    de la somme donnée en argument. Si la valeur séléctionnée peut être déduite, on sort de la boucle 
    et on recommence à parcourir la liste des différentes monnaie qu'on peut potentiellement rendre.
    On effectue cela jusqu'à ce que la somme mise en argument sois égale à 0.


    Entrée ------> une somme dont on veut connaître la somme a rendre

    Sortie ------> 
    '''
    monnaies = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    while argent > 0:
        for monnaie in monnaies:
            if monnaie <= argent:
                argent -= monnaie
                print(f'Il faut rendre {monnaie} euros')
                break

monnaie_a_rendre(595)

