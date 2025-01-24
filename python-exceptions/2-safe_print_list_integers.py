#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            # essaie d'afficher l'élément s'il est un entier
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            # Ignorer les éléments non entiers
            pass
    print("")  # Nouvelle ligne après l'affichage
    return count
