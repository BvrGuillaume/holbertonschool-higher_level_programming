#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:  # Si la liste est vide
        return None

    max_val = my_list[0]  # On initialise avec le premier élément
    for num in my_list:  # On parcourt tous les éléments
        if num > max_val:  # Si un élément est plus grand que max_val
            max_val = num  # On met à jour max_val
    return max_val  # On retourne la valeur maximale
