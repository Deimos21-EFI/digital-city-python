###########################
# Scan an OS folder and display files informations
###########################
import os
ignorePath = [".git", ".vscode", ".idea"]
def scanDir(pathToScan):
    #print(f"Scanning {pathToScan}")
    listOfFiles = os.listdir(pathToScan)
    listOfFiles = [f for f in listOfFiles if f.endswith(".py") or os.path.isdir(os.path.join(pathToScan, f))]
    fileType = ""
    for file in listOfFiles:
        # check if file is a directory
        fullPath = os.path.join(pathToScan, file)
        fileSize = ""
        if os.path.isdir(fullPath): fileType = "<DIR>"
        if os.path.isfile(fullPath):
            fileType = "<file>"
            fileSize = str(os.path.getsize(fullPath)) + " bytes"
        # pad the file name with spaces to align it in the print
        print(f"{fileType} {fileSize:>15} {fullPath}")
        try:
            ignored = (ignorePath.index(file) != -1)
        except:
            ignored = False
        if not ignored and os.path.isdir(fullPath):
            scanDir(fullPath)

mainPath="C:\\Users\\Worker\\Desktop\\python\\"
scanDir(mainPath)

###########################

