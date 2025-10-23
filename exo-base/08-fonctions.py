#########################################
# Méthodes : Fonctions / Procédures
#########################################
"""
Procédure - ne retourne aucune valeur
Fonction - retourne une valeur
"""
import math

import fonctions
from fonctions import *

# Méthodes built-in (intégrées)
texte = "      Bonjour brave Python 3.14       "
print("upper:" + texte.upper())
print("lower:" + texte.lower())
print("title:" + texte.title())
print("center:" + texte.center(50, "*"))
print("strip:" + texte.strip())
print("replace:" + texte.replace("Python", "Java"))
print("capitalize:" + texte.capitalize())
print("count 'o':" + str(texte.count("o")))
print(f"find 'Python': {texte.find("Python")}")
print(f"index 'Python': {texte.index("Python")}")

texte = texte.strip()
print(texte.split(" "))
listOfTexte = texte.split(" ")
print(f"splitted texte {listOfTexte}")
print(" ".join(listOfTexte))
# vérifier le contenu d'un texte
texte = "Éric"
print(f"isalpha: {texte.isalpha()}")
print(f"isalnum: {texte.isalnum()}")
texte = "31415"
print(f"isdecimal: {texte.isdecimal()}")
print(f"isdigit: {texte.isdigit()}")
print(f"islower: {texte.islower()}")
print(f"isspace: {texte.isspace()}")
print(f"istitle: {texte.istitle()}")
print(f"isupper: {texte.isupper()}")

title("Fonction Mathématique")

# Mathématique - nécessite d'importer un librairie (module)
value = math.pi
print(f"ceil:{math.ceil(value)}")
print(f"floor:{math.floor(value)}")
print(f"fabs:{math.fabs(value)}")
value = 5
print(f"factorial:{math.factorial(value)}")
print(f"pow:{math.pow(value, 2)}")
print(f"sqrt:{math.sqrt(value)}")

print(f"float absolue {math.fabs(math.pi)}")

##########################################
# Fonctions simple sans argument
title("Fonctions simple sans argument")
def printHello():
    print("Hello world")
printHello()
print(f"{printHello}")

###########################
# Fonctions avec argument
title("Fonctions avec argument")
def printHello(name):
    print(f"Hello {name}")

printHello("Python")

###########################
# Fonctions avec argument et valeur par défault
title("Fonctions avec argument")
def printHello(name = "nobody"):
    print(f"Hello {name}")

printHello("Python")
printHello()

##########################
# Function avec valeur de retour
title("Fonctions avec valeur de retour")
def fibo(count):
    strReturn = "0"
    v1 = 0
    v2 = 1
    for i in range(count):
        fibo = v1 + v2
        v1,v2 = v2, fibo
        strReturn += f", {fibo} "
    return strReturn

print(f"{fibo(5)}")
print(f"{fibo(10)}")


