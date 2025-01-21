#!/usr/bin/python3
def divisible_by_2(my_list=[]):
 # Initialise une liste vide pour stocker les résultats (True ou False)
    result = []
    
    # Parcourt chaque élément `x` de la liste `my_list`
    for x in my_list:
        # Vérifie si le nombre est divisible par 2
        if x % 2 == 0:
            # Si oui, ajoute True à la liste `result`
            result.append(True)
        else:
            # Sinon, ajoute False à la liste `result`
            result.append(False)
    
    # Retourne la liste contenant True ou False pour chaque élément
    return(result)
