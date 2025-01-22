#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Convertir la liste en un ensemble pour obtenir les entiers uniques
    uniq_numbers = set(my_list)
    # Calculer et retourner la somme des entiers uniques
    return sum(uniq_numbers)
