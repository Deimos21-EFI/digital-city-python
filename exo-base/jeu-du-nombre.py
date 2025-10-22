# Randow number
import random
from tarfile import data_filter


"""
Demander un nombre à l'utilisateur
- si le nombre est plus petit que la valeur random afficher (il est plus petit)
- si le nombre est plus grand que la valeur random afficher (il est plus grand)
"""
niveau = {
    "D" : "Difficile",
    "F" : "Facile"
}
print(niveau["D"])
print(niveau["F"])
def getValue():
    valueIsOk = False
    while not valueIsOk:
        myStrValue = input("Entrez votre nombre:")
        if (myStrValue.isdigit()):
            myValue = int(myStrValue)
            valueIsOk = True
        else:
            print(f"La valeur entrée n'est pas valide [{myStrValue}]")
    return myValue

def niveauDeDifficulte():
    print("Tapez D pour difficile et F pour facile")
    niveau = ""
    while niveau == "":
        niveau = input("Entrez votre niveau de difficulté : ").upper()
        if niveau != "D" and niveau != "F":
            print(r"/!\ Niveau de difficulté invalide. Tapez D ou F uniquement.")
    return niveau



def jouer():
    myValue = 0
    nbrOfTry = 0
    canPlay = True
    print("*****************************")
    print("Nous allons jouer au jeu du nombre mystère")
    print("Vous devez choisir un niveau de difficulté")
    print(" F - Facile : indication plus petit/grand et proximité")
    print(" D - Difficile : proximité uniquement")
    print("*****************************")
    difficulte = niveauDeDifficulte()
    print("*****************************")
    nbrRandom = random.randint(1, 100)
    # print(f"pour information, le nombre random est : {nbrRandom}")

    print("> J'ai choisi un nombre aléatoire, maintenant c'est à vous de jouer ...")
    print(f"> Vous avez choisi le niveau de difficulté {niveau[difficulte]}")
    print()
    myValue = getValue()
    diff = nbrRandom - myValue
    while diff != 0:
        nbrOfTry += 1
        if (difficulte == "F"):
            if (diff < 0 ):
                print(f"Le nombre entré {myValue} est plus grand que le nombre aléatoire")
            elif (diff > 0):
                print(f"Le nombre entré {myValue} est plus petit que le nombre aléatoire")

        if (abs(diff) < 5):
            print(f"Le nombre entré {myValue} est TRES proche du nombre aléatoire")
        elif (abs(diff) < 10):
            print(f"Le nombre entré {myValue} est proche du nombre aléatoire")
        elif (abs(diff) < 20):
            print(f"Le nombre entré {myValue} est éloigné du nombre aléatoire")
        elif (abs(diff) < 40):
            print(f"Le nombre entré {myValue} est fort éloigné du nombre aléatoire")
        elif (abs(diff) < 50):
            print(f"BRRR ! c'est galical - le nombre entré {myValue} est vraiment éloigné du nombre aléatoire")
        elif (abs(diff) < 80):
            print(f"WAOUH ! c'est une mauvaise journée - le nombre entré {myValue} est bien trop loin du nombre aléatoire")
        print("------------------------------")
        myValue = getValue()
        diff = nbrRandom - myValue

    print(f"BRAVO, le nombre entré {myValue} est égal au nombre aléatoire")
    print(f"Vous avez réussi après {nbrOfTry} essais")

jouer()
