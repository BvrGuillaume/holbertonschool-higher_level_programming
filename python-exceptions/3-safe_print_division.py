#!/usr/bin/python3
def safe_print_division(a, b):
    result = None
    try:
        result = a / b # Essaye de faire la division
    except ZeroDivisionError:
        result = None # Si division par zéro le résultat est None
    finally:
        print("Inside result: {}".format(result)) # Affiche le résultat ou None
    return result
