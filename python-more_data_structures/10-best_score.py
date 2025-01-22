#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:  # Vérifie si le dictionnaire est None ou vide
        return None
    # Trouve la clé correspondant à la plus grande valeur
    return max(a_dictionary, key=a_dictionary.get)
