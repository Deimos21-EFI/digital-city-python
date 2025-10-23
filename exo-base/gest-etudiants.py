label_etudiant = ["nom", "prenom", "age", "cours principal"]
import os
from  gestetudiantsactions import *


list_etudiant = dict(
    bob = ['Bob', 'Morane', 23, 'Python'],
    alice = ['Alice', 'Smith', 24, 'Java'],
    edgar = ['Edgar', 'Doe', 25, 'CSS'],
    jules = ['Jules', 'Doe', 26, 'HTML']
)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')




def remove_etudiants():
    print()
    print("Supprimer un étudiant")
    print("---------------------")
    a_supprimer = input("Quel étudiant voulez)vous supprimer ?")
    if (a_supprimer in list_etudiant):
        list_etudiant.pop(a_supprimer)
    else:
        print(f"Etudiant {a_supprimer } introuvable")

def modifier_etudiant():
    print()
    print("Modifier un étudiant")
    print("--------------------")
    cle_etudiant = input("Entrez le nom-clé de l'étudiant à modifier : ")
    if (cle_etudiant in list_etudiant):
        print("Tapez ENTER pour ne pas changer la valeur ou entrez la nouvelle valeur")
        info_etudiant = list_etudiant[cle_etudiant]
        for i in range(4):
            info = input(f"- {label_etudiant[i]} ({info_etudiant[i]}) : ")
            if (info != ""):
                info_etudiant[i] = info
        print("----- voici les nouvelles valeurs :")
        print(info_etudiant)
        sauver = input("-- Tapez Q pour annuler ou toute autre touche pour confirmer :")
        if (sauver.upper() == "Q"):
            print(f"Modification de l'étudiant {cle_etudiant} annulée")
        else:
            list_etudiant[cle_etudiant] = info_etudiant
            print(f"Modification de l'étudiant {cle_etudiant} effectuée")
    else:
        print(f"Etudiant {cle_etudiant} introuvable")

def add_etudiants():
    print()
    print("Ajouter un étudiant")
    print("-------------------")

    new_etudiant = input("Entrez le nom-clé de l'étudiant :")
    info_etudiant = []
    for i in range(4):
        info = input(f"{label_etudiant[i]} :")
        info_etudiant.append(info)

    list_etudiant[new_etudiant] = info_etudiant



#
# Main code
#
nePasQuitter = True

while nePasQuitter:
    print_menu()
    response = input("Que voulez-vous faire ? ")

    match response:
        case "1":
            print_etudiants()
        case "2":
            add_etudiants()
        case "3":
            modifier_etudiant()
        case "4":
            remove_etudiants()
        case "5":
            nePasQuitter = False
    if nePasQuitter:
        pause()
        clear_screen()

