#!/usr/bin/python3
def safe_print_integer(value):
    try:
        # Essaie de formater et d'imprimer `value` comme un entier
        print("{:d}".format(value))
        return True
    # Si exception retourne false
    except (ValueError, TypeError):
        return False
