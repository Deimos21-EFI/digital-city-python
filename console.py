#########################
# Console
#########################

print("texte")

name="Michael Jordan"
print (name)
print (f"name : {name}")

print ("Result of 5*3=", 5*3)
print (f"Result of 5*3={5*3}")

intValue = 1
textValue = "My text "
print (textValue + intValue.__str__())
print (f"Écho {textValue} + {intValue}")

print(r"C:\Users\Worker")

print ("un", 'deux', "trois", sep=",", end=";")

print ()
#########################
# input values
#########################

name = input("Entrez votre nom:")
print(f"bonjour {name} ({type(name)}), bienvenue")
# Convertion str -> int
age = input("Quel est votre âge ?:")
age = int(age)
print(f"Votre âge est {age} ({type(age)})")
# Convertion int -> str
age_str = str(age)
print(f"Votre âge est {age_str} ({type(age_str)})")