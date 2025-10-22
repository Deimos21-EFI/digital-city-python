###########################
# structure conditionnelles
###########################
"""
# IF
 if bool:<instruction>

 if bool:
    <instructions>

 if bool:
    <instructions>
 elif bool:
    <instructions>
 elif bool:
    <instructions>
 else:
    <instructions>

"""
import datetime
import time
from turtledemo.sorting_animate import instructions1

"""
age = int(input("Enter your age:"))

if (age < 18):
    print("You are a minor")
elif (age < 25):
    print("You are an adult but still junior ")
elif (999 > age > 65):
    print("You are third age")
else:
    print("You are an adult")
"""
################
# match (switch)
"""
match variable
    case value1:
        instructions1
    case value2: 
        instructions2
    case value3 | value4:
        instructions3
    case _:
        defaultinstruction

"""
################

jourDeLaSemaine = 6

match jourDeLaSemaine:
    case 1: print("Lundi")
    case 2: print("Mardi")
    case 3: print("Mercredi")
    case 4: print("Jeudi")
    case 5: print("Vendredi")
    case 6 | 7: print("Week End")
    case _: print("Jour de la semaine invalide")
    
    
###########################
# structure conditionnelles
###########################

#####
# FOR in loop
"""
for variable in list:
    instructions
"""
#####

fruits = ["pomme", "fraise", "poire", "arbricot", "cerise", "banane"]

print(fruits)
print(fruits[0])
print(len(fruits))
print("liste des fruits")
for f in fruits:
    print(f)

# copy fruits in another list
print("Copie de fruits inversée")
copyFruits = fruits.copy()
copyFruits.reverse()
for f in copyFruits:
    print(f)

for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# range (from 0 to 9)
print("range (from 0 to 9)")
for i in range(10):
    print(i)

# range (from 5 to 10)
print("range (from 5 to 10)")
for i in range(5, 11):
    print(i)
else:
    print("end of loop")

# range (from 5 to 10)
print("range (from 1 to 21)")
for i in range(0, 21, 5):
    print(i)
else:
    print("end of loop - step 5")

#######################################
# while -
"""
  while <condition>:
    instructions
    break
    continue
    else:
        instructions
"""

depart, fin = 1, 100000
#display the time start in seconds
tStart = time.time()
print("start time")
while depart <= fin:
    #print(f"valeur: {depart}")
    depart += 1
else:
    tEnd = time.time()
    print(f"duration {(tEnd-tStart) * 1000:.2f}" )

# verification de l'entrée de l'utilisateur
inputUserDay = ""
isCorrect = False
while not isCorrect:
    inputUserDay = input("🗓️ Entrez un jour de la semaine (1-7): ")
    try:
        inputUserDay = int(inputUserDay)
        isCorrect =  (1 <= inputUserDay <= 7)
        if (not isCorrect): print("⚠️ Jour de la semaine invalide")
    except ValueError:
        print("❌ Veuillez entrer un nombre valide")
else:
    print(f"Bravo ! vous avez réussi à introduire un jour de la semaine 👌")

