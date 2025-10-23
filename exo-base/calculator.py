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

from fonctions import *

setDebug(False)
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

nombre = getEntier()

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
        #if (strResultat == ""):
        #    strResultat = f"{nombre}"
        #else:
        strResultat += f"{nombre}" + operator
        print(f"🧮 {strResultat}")
        #
        # Lire le nombre suivant
        #
        nombre = getEntier()
        debug("-------")
else:
    # afficher le résultat final
    #strResultat +=  f"{nombre}" + operator
    print(f"🟰 {strResultat} = {intResultat}")
######################################################