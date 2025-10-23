DEBUG = True

def setDebug(value):
    """
    Activer l'affichage des messages de debug
    :param value: boolean (True/False)
    :return:
    """
    global DEBUG
    if (isinstance(value, bool)):
        DEBUG = value

def title(text):
    print(f"\n### {text.center(50, '-')} ###\n")

def printHello():
    print("Hello world")

def printHelloName(name="<unknown>"):
    print(f"Hello {name}")


def debug(msg):
    if DEBUG:print(f"[INFO]: {msg}")

def getOperator():
    """
    Demande à l'utilisateur une opération et retourne le symbole de l'opération
    """
    operation = ""
    operationValide = False
    while not operationValide:
        operation = input("Entrez une opération (+, -, *, /) : ")
        #operationValide = (operation == "=" or operation == "+" or operation == "-" or operation == "*" or operation == "/")
        operationValide = ("+-*/=".find(operation) >=0)
        if operationValide == False: print("[ERROR] Invalid operator")
    else:
        return operation

def getEntier():
    """
    Demande à l'utilisateur un nombre entier et retourne la valeur numérique
    :return: nombre
    """
    valueIsOk = False
    while not valueIsOk:
        myStrValue = input("Entrez un nombre entier:")
        try:
            myValue = int(myStrValue)
            valueIsOk = True
        except:
            print(f"La valeur entrée n'est pas valide [{myStrValue}]")
    else:
        return myValue

def pause():
    input("Appuyez sur ENTREE pour continuer...")
