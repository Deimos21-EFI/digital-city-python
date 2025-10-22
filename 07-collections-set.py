###################################################
# set
# ensemble non ordonnées d'éléments uniques
#
# help(set)
animaux = {'chien', 'chat', 'chien', 'chat', 'chien', 'chat', 'chien'}
print(animaux)
print(len(animaux))

animaux.add("poule")
print(animaux)

animaux.update(["hamster", "canari"])
print(animaux)

animaux.update({"souris", "rat"})
print(animaux)

animaux.remove("chien")
print(animaux)

alaFerme={"poule", "vache", "chèvre", "lapin"}
diff = animaux.difference(alaFerme)
print("--- diff")
print(alaFerme)
print(animaux)
print(diff)
print(alaFerme.difference(animaux))

print("--- in")
print(animaux)
print("chien" in animaux, animaux)

fruits = ['banane', 'orange', 'pomme', 'poire', 'fraise']

print("banane" in fruits, f"banane in {fruits}")

fruits1 = {'banane', 'orange', 'pomme', 'poire', 'fraise'}
fruits2 = {'ananas', 'cerise', 'pêche', 'poire', 'fraise'}
fruits1.difference_update(fruits2)
print(fruits1)

print(f"{fruits2} contient 'ananas'", fruits2.__contains__("ananas"))
