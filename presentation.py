############
# récupération du nom, de l'âge et du hobby
####
# déclaration
"""
name, age, hobby = "", "", ""
# recupération
name = input("Enter your name:")
age = input("What is your age:")
hobby = input("What is your preferred hobby:")
# affichage
print(f"Hello {name}, you are {age} and your preferred hobby is {hobby}.")
"""
def inputValue(displayText, isMandatory="0"):
    """
    Display a text and request a value.
    When isMandatory is true, the user muste enter a value

    :param dataType:
    :param displayText: Text to display within the input
    :param isMandatory: when true, user must enter something
    :return:
    """
    continueLoop = True
    value = ""
    isMandatory = (isMandatory == "1")
    while (continueLoop):
        value = input(displayText)
        if (isMandatory and value == ""):
            print("value is mandatory")
        else:
            continueLoop = False
    return value

def inputText(displayText, isMandatory="0"):
    return inputValue(displayText, isMandatory)

def inputNumber(displayText, isMandatory="0"):
    isNumber = False
    returnValue = ""
    while (not isNumber):
        returnValue = inputValue(displayText, isMandatory)
        if (returnValue.isdigit()):
            returnValue = int(returnValue)
            isNumber = True
        else:
            print(f"Value is not a number - got [{returnValue}]")
    return returnValue

def displayIdentity(pIdentity, displayRaw="0"):
    if (displayRaw != "1"):
        print(f"Hello {pIdentity["name"]}")
        if (pIdentity["age"] != ""):print(f"You are {pIdentity["age"]}")
        if (pIdentity["hobby"] != ""):print(f"And your preferred hobby is {pIdentity["hobby"]}")
    else:
        print(f"[INFO] raw value: {pIdentity}")


identity = {
    "name" : "",
    "age" : 0,
    "hobby" : ""
}
identity["name"] = inputValue("Enter your name:", "1")
identity["age"] = inputNumber("What is your age:")
identity["hobby"] = inputValue("What is your preferred hobby:")
identity["other"] = inputValue("give me an other info:")
# affichage
displayIdentity(identity)
displayIdentity(identity, "1")
#print(f"Hello {identity["name"]}, you are {identity["age"]} and your preferred hobby is {identity["hobby"]}")
#print(f"{identity}")



def action2(a,b,c):
    print(f" voici les valeurs : {a} , {b} ")