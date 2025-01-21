#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    # Vérifie si idx est négatif ou non
    if idx < 0 or idx >= len(my_list):
        # Si idx est invalide, retourne la liste originale sans modification
        return my_list  
    
    # Supprime l'élément à la position spécifiée dans la liste
    del my_list[idx]  
    
    # Retourne la liste modifiée
    return my_list
