##################################
#
"""
# Variables
- name
  - doivent commencer par une lettre ou un underscore
  - uniquement des caractères alphanumérique et underscore
  - cas sensitive
- value
- type
  - int, float, str, bool
  - tuple, list, dict
  - object, function

type() : allow to get the variable type

# Constantes
- Constant does not exist in python
"""
##################################

my_var_num = 1
myVarNum = 2

print(f"my_var_num: {type(my_var_num)}")
print(f"myVarNum: {type(myVarNum)}")
#print("myVarNum:" + type(myVarNum))

"""
# Variable Types
## simple
- int 
- float
- str
- bool
## array
- tuple ensemble de valeur
- list tableau [1, 2, ...]
- dict : dictionnaire {"clé", "valeurs"} = {"1", "bob"}
## object
- object 
- function 
## null
- None absence de vakeur (null)


"""

intVar = 25
floatVar = 3.141539
boolVar = True # True / False
tupleVar = (4,5,6)
print(f"tuple {tupleVar}")

listVar = []
listVar.append("Texte")
listVar.append(100)
print(f"listVar {listVar}")

dictVar = {
    "nom" : "ALBERT",
    "prénom" : "premier"
}
print(f"dictVar {dictVar}")

objVar  = object()
objVar = {
    "nom" : "",
    "prénom" : "",
    "adresse" : ""
}
print(f"objVar {objVar}")

nullVar = None

functionVar = lambda x: x*2

square = lambda x: x*x


print(f"function lambda {functionVar(5)}")


# declaration and assignment
x = 5
a,b,c = 1,2,3

print(a, b, c)