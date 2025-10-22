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

DEBUG = True

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
        #operationValide = (operation == "=" or operation == "+" or operation == "-" or operation == "*" or operation == "/")
        operationValide = ("+-*/=".find(operation) >=0)
        if operationValide == False: print("[ERROR] Invalid operator")
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
#
# Initialisation
#
strResultat=""
intResultat = 0
operator = ""
finDeCalcul = False

nombre = getNombre()

while not finDeCalcul:
    debug(f"Nombre saisi : {nombre}")
    operator = getOperator()
    if (operator == "="):
        finDeCalcul = True
    else:
        # cas: déjà un calcul effectué
        match operator:
            case "+":
                debug(f"+ Addition de {nombre} à {intResultat}")
                intResultat += nombre
            case "-":
                debug(f"+ Soustraction de {nombre} à {intResultat}")
                intResultat -= nombre
            case "*":
                debug(f"+ Multiplication de {intResultat} par {nombre} ")
                intResultat *= nombre
            case "/":
                debug(f"+ Division de {intResultat} par {nombre}")
                intResultat /= nombre
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
        nombre = getNombre()
        debug("-------")
else:
    # afficher le résultat final
    print(f"🟰 {strResultat} = {intResultat}")
    print(f"{3+4}")
######################################################