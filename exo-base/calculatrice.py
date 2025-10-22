######################################################
# Calculatrice
######################################################
# - Gérer les opérations simples : + - * /
# - Demander à l'utilisateur un premier nombre
# - Boucler
# - L'utilisateur va introduire un opérateur puis un nombre
# - Le résultat contient la valeur du calcul
# - calcul (str) qui va enregistrer toutes les opérations
# - afficher le résultat si l'utilisateur entre le "="
#
# resultat = resultat + 1
# resultat = resultat + 1
# resultat = resultat + 1
# resultat = resultat + 1
# resultat = resultat + 1
# resultat = resultat + 1

######################################################

DEBUG = False

def debug(msg):
    if DEBUG:print(f"[INFO]: {msg}")

def getOperator():
    """
    Demande à l'utilisateur une opération et retourne le symbole de l'opération
    """
    operation = ""
    operationValide = False
    while not operationValide:
        operation = input("Entrez une opération (+, -, *, /) : ")
        operationValide = (operation == "=" or operation == "+" or operation == "-" or operation == "*" or operation == "/")
        operationValide = "+-*/".find(operation)
    else:
        return operation

def getNombre():
    """
    Demande à l'utilisateur un nombre et retourne la valeur numérique
    :return: nombre
    """
    valueIsOk = False
    while not valueIsOk:
        myStrValue = input("Entrez votre nombre:")
        if (myStrValue.isdigit()):
            myValue = int(myStrValue)
            valueIsOk = True
        else:
            print(f"La valeur entrée n'est pas valide [{myStrValue}]")
    else:
        return myValue

print("Calculatrice")
print("------------")
print("ℹ️ Instruction:")
print("▫️Entrez un nombre et puis une opération, le calcul est affiché au fur et à mesure")
print("▫️Entrez = pour terminer le calcul")
print("------------")

strResultat=""
resultat = 0
finDeCalcul = False
operator = ""
debut = True
oldResultat = 0
nombre = getNombre()
while not finDeCalcul:
    debug(f"Nombre saisi : {nombre}")
    if (strResultat == ""):
        # cas: pas encore de calcul
        resultat = nombre
    else:
        oldResultat = resultat
        # cas: déjà un calcul effectué
        if (operator == "="):
            debug(f"Résultat: {resultat}")
            finDeCalcul = True
        elif (operator == "+"):
            debug(f"+ Addition de {nombre} à {resultat}")
            resultat += nombre
        elif (operator == "-"):
            debug(f"+ Soustraction de {nombre} à {resultat}")
            resultat -= nombre
        elif (operator == "*"):
            debug(f"+ Multiplication de {resultat} par {nombre} ")
            resultat *= nombre
        elif (operator == "/"):
            debug(f"+ Division de {resultat} par {nombre} ")
            resultat /= nombre
    #
    # Afficher le résultat intermédiaire
    #
    if (strResultat == ""):
        strResultat = f"{nombre}"
    else:
        strResultat += operator + f"{nombre}"
    print(f"🧮 {strResultat}")
    #
    # Lire le nombre suivant
    #
    operator = getOperator()
    if (operator == "="):
        finDeCalcul = True
    else:
        nombre = getNombre()
    debug("-------")
else:
    # afficher le résultat final
    print(f"🟰 {strResultat} = {resultat}")
    print(f"{3+4}")
######################################################