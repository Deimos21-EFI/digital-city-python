###################################
# Gestion des livres
import uuid

from fonctions import *

###################################
# Variables
###################################

labels = ["id", "titre", "auteurs", "isbn", "editeur"]
tailles = {"id": 5, "titre": 40, "auteurs": 30, "isbn": 17, "editeur": 20}
#livres = dict()
livres = []
saved = False
vert = "\033[32m"
rouge = "\033[31m"
normal = "\033[0m"
blue = "\033[34m"
clearscreen = "\033[H\033[J"
"""
list_book = []

book = dict(
    id = 1234,
    autor = "John Doe",
    nbPages = 123,
)
list_book.append(book)

for book in list_book:
    print(book["id"])
    print(book["id"])

def add_book():
    # recuperer les valeurs
    # creation du livre
    # ajouter le livre a la liste
"""


###################################
# Fonctions
# charger la liste / sauver la liste
# afficher la liste
# ajouter un livre
# supprimer un livre
# modifier un livre
###################################

# Convert the string "{'id': '37', 'titre': 'Titre 37', 'auteurs': '', 'isbn': '', 'editeur': ''}" into an object dict
def convertStringToDict(string):
    return eval(string)


def chargerLivres():
    """
    Charger les livres depuis un fichier
    :return:
    """
    loadFromFile()


def loadFromFile():
    """
    Charger les livres depuis un fichier "livres.dict"
    :return:
    """
    f = open("livres.dict", "r", encoding="utf-8")
    while (ligne := f.readline().strip()):
        livre = dict()
        livre = eval(ligne)
        livres.append(livre)
    f.close()


def saveToFile():
    """
    Sauvegarder les livres dans un fichier "livres.dict"
    :return:
    """
    f = open("livres.dict", "w", encoding="utf-8")
    #headerLine = ",".join(labels)
    #f.write(headerLine + "\n")
    for livre in livres:
        f.write(f"{livre}\n")
    f.close()


def afficherMenu():
    """
    Afficher le menu de gestion des livres
    :return:
    """
    print(f"${clearscreen}")
    print("".center(50, "-"))
    print("Menu de la gestion des livres".center(50))
    print("".center(50, "-"))
    print(f"| 1. 📋 Afficher la liste des livres")
    print(f"| 2. ➕ {vert}Ajouter un livre{normal}")
    print(f"| 3. 🔃 {vert}Modifier un livre{normal}")
    print(f"| 4. ❌ {rouge}Supprimer un livre{normal}")
    print(f"| 5. 💾 {blue}Enregistrer les livres{normal}")
    print(f"| Q. 🔚 Quitter")
    print("".center(50, "-"))


def votreChoix():
    """
    Demander à l'utilisateur de saisir son choix
    :return: le choix le l'utilisateur
    """
    choix = input(">>> Entrez votre choix : ")
    return choix


def getShortUniqueId():
    return str(uuid.uuid4())[:8]


def afficherLivres():
    """
    Afficher la liste des livres avec mise en forme
    """
    print("".center(50, "-"))
    print("Liste des livres".center(50))
    print("".center(50, "-"))

    for livre in livres:
        strLigne = ""
        for item in livre:
            taille = tailles[item]
            strLigne += f"{livre[item]:<{taille}} | "
        print(f"| {strLigne}")


def ajouterLivre():
    print("".center(50, "-"))
    print("Ajouter un livre".center(50))
    print("".center(50, "-"))
    print("Entrez les données du livre")
    try:
        livre = dict()
        for label in tailles:
            texte = input(f"{label} : ")
            livre[label] = texte
        livres.append(livre)
    except Exception as e:
        print(f"[ERROR] - ajouterLivre - {e}")



def modifierLivre():
    """
    Modifier un livre sur base de son ID
    :return:
    """
    print("".center(50, "-"))
    print("Modifier un livre".center(50))
    print("".center(50, "-"))
    livreId = input("Entrez l'ID du livre à modifier : ")
    livreToUpdate = None
    for livre in livres:
        if livre["id"] == livreId:
            livreToUpdate = livre
            break

    if livreToUpdate != None:
        # Si le livre est trouvé, on peut le modifier
        livre = livreToUpdate.copy()
        for label in tailles:
            texte = input(f"{label} ({livre[label]}): ")
            match texte:
                case "":
                    pass
                case "-":
                    livre[label] = ""
                case __:
                    livre[label] = texte
        livres.remove(livreToUpdate)
        livres.append(livre)
    else:
        print(f"⚠️ Ce livre [{livreId}] n'est pas dans la liste")


def supprimerLivre():
    """
    Supprimer un livre sur base de son ID
    :return:
    """
    print("".center(50, "-"))
    print("Supprimer un livre".center(50))
    print("".center(50, "-"))
    livreId = input("Entrez l'ID du livre à supprimer : ")
    livreToUpdate = None
    for livre in livres:
        if livre["id"] == livreId:
            livreToUpdate = livre
            break

    if livreToUpdate != None:
        # Si le livre est trouvé, on peut le supprimer
        livres.remove(livreToUpdate)
        print(f"✅ Le livre [{livreId}] a été supprimé avec succès")
    else:
        print(f"⚠️ Ce livre [{livreId}]n'est pas dans la liste")


def confirmeQuitter():
    """
    Demander confirmation de quitter si les données ne sont pas sauvées
    :return:
    """
    reponse = input("⚠️ Les données ne sont pas enregistrées, Voulez-vous quitter ?\n(O pour confirmer) : ").upper()
    return reponse == "O"


#
#
#
def gestionDesLivres():
    """
    Module de gestion des livres - écran principal
    :return:
    """
    chargerLivres()
    quitter = False
    saved = True
    while not quitter:
        afficherMenu()
        print(f"unique id : {getShortUniqueId()}")
        monChoix = votreChoix().upper()

        match monChoix:
            case "1":
                afficherLivres()
                pause()
            case "2":
                ajouterLivre()
                saved = False
            case "3":
                modifierLivre()
                saved = False
            case "4":
                supprimerLivre()
                saved = False
            case "5":
                saveToFile()
                saved = True
            case "Q":
                quitter = True
                if not saved:
                    quitter = confirmeQuitter()
    else:
        print("Fin du programme")


###################################
#
###################################
gestionDesLivres()
###################################
