###############################################
# Collections
"""
Les collections = structure de données permettant de gérer des ensembles de données.
 - les listes
 - les dictionnaires
 - les tuples
 - les sets
"""
###############################################

#
# Les listes
# - Collections modifiables
# - Peuvent contenir des données de type différents
# - Géré par des index/indice de 0 à n
# help(list)

fruits = ['banane', 'orange', 'pomme', 'poire', 'fraise']

# index ou indice  liste[<valeur>]
print("------------------ index ou indice  liste[<valeur>]")
print(fruits[0])

# boucle dans une liste
print("------------------ boucle dans une liste")
for f in fruits:
    print(f)

# boucle dans une liste avec enumeration
print("------------------ boucle dans une liste avec enumerate")
for idx, value in enumerate(fruits):
    print(f"{idx} = {value}")

# ajouter dans la liste
print("------------------ ajouter dans la liste")
fruits.append("kiwi")
print(fruits)
# insérer dans la liste
print("------------------ ajouter dans la liste")
fruits.insert(0, "citron")
print(fruits)
# retirer de  la liste
print("------------------ retirer de  la liste")
fruits.remove("pomme")
print(fruits)
# retirer le dernier de la liste
print("------------------ retirer le dernier de la liste")
fruits.pop()
print(fruits)
# retirer un élément précis de la liste
print("------------------ retirer un élément précis de la liste")
fruits.pop(1) # banane
print(fruits)
# gestion d'une erreur dans le remove
print("------------------ gestion d'une erreur dans le remove ['rien']")
try: fruits.remove("rien")
except ValueError: print("le fruit n'existe pas dans la liste")
print(fruits)
print("------------------ Retirer avec del")
del fruits[0]
print(fruits)

# faire un copie de la liste
print("------------------ faire un copie de la liste")
print("------------------ faire un copie de la liste")
fruitsCopy = fruits.copy()
print(fruitsCopy)
print(fruits)
copyFruitsByRef = fruits # copie par réference les 2 sont les mêmes entités


# Vider une liste
print("------------------ Vider une liste")
fruitsCopy.clear()
print(fruitsCopy)
print(fruits)

# Inverser la liste
print("------------------ Inverser la liste")
fruits.reverse()
print(fruits)

# Trier la liste
print("------------------ trier la liste")
fruits.sort()
print(fruits)

# Démo copie byref vs valeur
print("------------------ Démo copie byref vs valeur")
liste_originale = [1, 2, 3, 4, 5]
liste_copie = []
# copie la référence
liste_copie = liste_originale
# copie des valeurs (slicing)
liste_copie = liste_originale[:]
# copie par valeur
liste_copie = liste_originale.copy()
# via le constructeur
liste_copie = list(liste_originale)
liste_copie = list(["info1", "info2", "info3"])

liste2 = ["a", "b", "c"]
liste2 += liste_copie[:]
print(liste2)

##
# Slicing
# - permet de récupérer tout un partie d'une liste
# - list[start:stop:step] (start inclus, stop exclus)
# - la liste débute à ZERO

l1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"l1 = {l1}")
print(f"l1[:5] = {l1[:5]}")   # les 5 premiers
print(f"l1[2:5] = {l1[2:5]}") # du 2e au 5e non inclus
print(f"l1[2:] = {l1[5:]}")   # du 2e au fin
print(f"l1[2:] = {l1[:3]+l1[8:]}")   # les 3 premiers et les 3 derniers
print(f"l1[2:] = {l1[:1]+l1[-1:]}")   # le premier et le dernier

liste_debut_fin = l1[:1] + l1[-1:]


#
# ajouter dans la liste via un input
#
# initialisation
bContinue = True
myList = []
# boucle
while bContinue:
    # ajouter dans la liste
    newData = input("Entrer un nouvelle données : ")
    try:
        myList.index(newData)
        print("⚠️ {newData} est déjà dans la liste")
    except:
        myList.append(newData)

    print(myList)
    # Faut-il continuer ?
    response = input("Voulez-vous continuer ? [enter/O] = continue, C(lear)  : ")
    bContinue = (response.upper() == "O" or response == "")
else:
    print("fin de la boucle")





"""
for key, value in fruit:
    print(f"{key}: {value}")
"""