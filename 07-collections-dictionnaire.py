############################
# Dictionnaire
# clé, valeur
#

#déclaration

etudiant1 = {
    "name": "John",
    "age": 23,
    "cours": ["Python", "Java", "CSS"]
}

etudiant2 = dict(
    name = "Morane",
    firstname = "Bob",
    age = 25,
    cours = ["Python", "Java", "CSS"]
)
print("------------- etudiant1")
print(etudiant1)
print(etudiant1["name"])
print("------------- etudiant2")
print(etudiant2)
print(etudiant2["name"])
print(etudiant2["firstname"])
for cours in etudiant2["cours"]:
    print(cours)
print("------------- dictionnaire")
etudiants = dict()

etudiants["1"] = etudiant1
etudiants["2"] = etudiant2
etudiants["3"] = ""

print(etudiants)
print(etudiants["1"])
print(etudiants["2"])

print("------------- modification")
etudiant1["age"] = 24
etudiant1["adresse"] = "Grand Rue, 24"
print(etudiants["1"])

print("------------- parcourir le dictionnaire")
for key, value in etudiants.items():
    print(f"key: {key}, value: {value}")
    for attribut in value:
        print(f"type of attribute is {type(attribut)}")
        if (isinstance(attribut, list) ):
            for attrItem in attribut:
                print(f"  - attribut: {attrItem} = {value[attribut]}")
        else:
            print(f"- attribut: {attribut} = {value[attribut]}")

print("------------- parcourir le dictionnaire")
for item in etudiants.items():
    print(f"item: {item}")
    key, value = item
    print(f"key: {key}, value: {value}")

print("------------- parcourir le dictionnaire par clé")
for key in etudiants.keys():
    print(f"key: {key}")
    print(f"etudiants[{key}] {etudiants[key]}")
