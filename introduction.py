# Introduction
def myfunction():
    print ("Hello world")

# docstring : accès aux informations de la fonction
def addition(a,b):
    """
    Additionne a et b et retourne le résultat
    :param a: Entier
    :param b: Entier
    :return:
    """
    return a+b

"""
Multiline comments
Cool ça marche
Demande un nom et affiche le
"""
# génère l'aide de la fonction
help (addition)
# affiche la doc liée à la fonction
print(addition.__doc__)

#########################################
# Imports
#########################################
# importe la librairie complète
import math

# importe une partie spécifique de la librairie
from math import pi

# liste des installations
# pip list (dans le terminal)
#
# https://docs.python.org/3/py/modindex.html

print ("Le nom " + __name__)
if __name__ == '__main__':
    print("c'est le main")