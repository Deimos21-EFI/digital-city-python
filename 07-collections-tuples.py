###################################
# tuples : permet de renvoyer plusieurs valeurs
# - immuables
# help(tuple)

myTuple = (10,20,30)
myStrTuple = ("a", "b", "c", "d", "e")
print(myTuple)

v1, v2, v3 = myTuple
print(f"v1: {v1}, v2: {v2}, v3: {v3}")

print (myTuple[0])

# parcourir les tuples
for v in myStrTuple:
    print(f"v: {v}")