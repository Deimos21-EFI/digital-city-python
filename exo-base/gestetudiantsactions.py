
#
def print_etudiants():
    """

    :return:
    """
    print()
    print("Voici la liste des étudiants")
    print("----------------------------")
    for etudiant in list_etudiant:
        print(f"{etudiant}: {list_etudiant[etudiant]}")
    print("---")

def print_menu():
    print("Menu:")
    print("1. Afficher la liste des étudiants")
    print("2. Ajouter un étudiant")
    print("3. Modifier un étudiant")
    print("4. Supprimer un étudiant")
    print("5. Quitter")