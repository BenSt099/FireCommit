###############################################
################### Imports ###################
###############################################


import os
import sys
import time
import json
import subprocess
from pathlib import Path
from datetime import date
from datetime import datetime


###############################################
################## READ JSON ##################
###############################################


def getDataFromJSONConfigFile(filename):
    with open(filename, "r", encoding="utf-8") as out:
        data = json.load(out)    
    return data


###############################################
################### PRE-Push ##################
###############################################

prepush = """
if [[ $exit_code -ne 0 ]]; then
    echo "Checks failed. Push aborted."
    exit 1
fi

exit 0
"""

def createPrePushHook(executeCommand):
    pathtohook = ".git/hooks/pre-push"
    rootdir = Path(os.getcwd()).parent.absolute()
    path =  os.path.join(rootdir, pathtohook)
    if os.path.exists(path):
        return 1

    with open(path, "w") as f:
        f.write("#!/bin/sh\n")
        f.write("echo 'Checking...'\n")
        f.write(executeCommand + "\n")
        f.write(prepush)
    return 0


###############################################
############## Support Functions ##############
###############################################


def getModificationsFromFiles():
    returnStr = subprocess.run("git diff --staged --stat", capture_output=True, text=True,shell=True)
    return returnStr.stdout


def saveToFile(commitMsg):
    save = input(">>> Save To File And Not Commit [Y | N] ? ")
    if(save == "y" or save == "Y"):
        with open("commit-msg.txt", "w", encoding="utf-8") as outputFile:
            outputFile.write(commitMsg)
        exitScript()

def check2():
    try:
        returnStr = subprocess.run("git status", capture_output=True, text=True,check=True,shell=True)
        returnStr.check_returncode()
    except subprocess.CalledProcessError: 
        return "❌ This is not a git repository !"
    return "✅ Everything ok !"


def checkIfCurrentDirIsGitRepo():
    print()
    print("⚬ Checking if this is a git repository...")
    print()

    try:
        returnStr = subprocess.run("git status", capture_output=True, text=True,check=True,shell=True)
        returnStr.check_returncode()
    except subprocess.CalledProcessError: 
        print("❌ This is not a git repository !")
        time.sleep(5)
        exitScript()
    print("✅ Everything ok !")
    print()


def assembleCommitMSGFromFile():

    data = getDataFromJSONConfigFile(os.path.join(os.getcwd(), "msgstructure.json"))
    msg = getCommitTopic() + " | 🔑 " + getKeywords() + "\n\n"
    
    for d in data.keys():
        if d == "Author" and data.get(d) == True:    
            msg = msg + "👥 AUTHOR".ljust(12) + getAuthorS() + "\n"
        elif d == "Scope" and data.get(d) == True:
            msg = msg + "🛠️  SCOPE".ljust(12) + getScope() + "\n" 
        elif d == "Branch" and data.get(d) == True:
            msg = msg + "🔱 BRANCH".ljust(12) + getWorkingBranch() + "\n\n"
        elif d == "Changes" and data.get(d) == True:
            msg = msg + getListOfChanges() + "\n\n"
        elif d == "Modifications" and data.get(d) == True:
            msg = msg + getModificationsFromFiles() + "\n\n"
        elif d == "Date" and data.get(d) == True:
            msg = msg +  getCurrentDate() + " " 
        elif d == "Time" and data.get(d) == True:
            msg = msg +  getCurrentTime() + " "     
    return msg

def check1():
    try:
        returnStr = subprocess.run("git status", capture_output=True, text=True,check=True,shell=True)
        returnStr.check_returncode()
    except subprocess.CalledProcessError: 
        return "❌ Checking for unstaged commits failed !"

    if(returnStr.stdout.find("Changes not staged") != -1):
        return "❌ Found Unstaged Files !"
    else:
        return "✅ Everything Clean !"


def checkForUnstagedFiles():
    print("""
    ⚬ Checking for unstaged files...
    """)
    print()
    try:
        returnStr = subprocess.run("git status", capture_output=True, text=True,check=True,shell=True)
        returnStr.check_returncode()
    except subprocess.CalledProcessError: 
        print("❌ Checking for unstaged commits failed !")
        print()
        print("⚠️ Committing might not work.")
        print()

    if(returnStr.stdout.find("Changes not staged") != -1):
        print("❌ Found Unstaged Files !")
        print()
    else:
        print("✅ Everything Clean !")


def runGitCommit(inputMsg):
    print()
    print("___________________________________________")
    print("Commit Message: \n")
    print(inputMsg)
    print()
    print("___________________________________________")
    print()
    checkForUnstagedFiles()
    print()
    saveToFile(inputMsg)
    print()
    inputStr = input(">>> Proceed [Y | N] ? ")

    if(inputStr == "N" or inputStr == "n"):
        exitScript()

    print("⚬ Trying to commit...")
    print()
    secParam = "git commit -m \"" + inputMsg + "\""

    if sys.platform.startswith('win32'):
        try:
            retCode = subprocess.run(secParam, check=True) # windows
        except subprocess.CalledProcessError:
            print("❌ Commit - Failure !")
    elif sys.platform.startswith('linux'):
        try:
            retCode = subprocess.run(secParam,shell=True,check=True) # linux
        except subprocess.CalledProcessError:
            print("❌ Commit - Failure !")
    elif sys.platform.startswith('darwin'):
        try:
            retCode = subprocess.run(secParam,shell=True,check=True)
        except subprocess.CalledProcessError:
            print("❌ Commit - Failure !")

    try:
        retCode.check_returncode()
    except subprocess.CalledProcessError: 
        print("❌ Commit - Failure !")
        time.sleep(10)
        exitScript()

    print("✅ Commit - Successful !")    


def push():
    try:
        retCodePush = subprocess.run("git push",check=True,shell=True)
        retCodePush.check_returncode()
    except subprocess.CalledProcessError: 
        #print("❌ Pushing - Failure !")
        time.sleep(5)
        #exitScript()

    #print("✅ Pushing - Successful !")


def runGitPush():
    print()
    runGitPush = input(">>> Run Git Push [Y | N] ? ")
    if(runGitPush == "N" or runGitPush == "n"):
        exitScript()

    print("⚬ Trying to push...")
    print()
    try:
        retCodePush = subprocess.run("git push",check=True,shell=True)
        retCodePush.check_returncode()
    except subprocess.CalledProcessError: 
        print("❌ Pushing - Failure !")
        time.sleep(5)
        exitScript()

    print("✅ Pushing - Successful !")


###############################################
############## Parts Of COM-MSG ###############
###############################################


def getTopicsAsList():
    data = getDataFromJSONConfigFile(os.path.join(os.getcwd(), "committopics.json"))
    ll = [data.get(d) for d in data.keys()]
    ll.insert(0, "Default: UP(⬆️)")
    return ll

def getCommitTopic():  
    
    data = getDataFromJSONConfigFile("committopics.json")
    print()

    print("Possible 📋 TOPIC: \n")
    
    for d in data.keys():
        print(d + " - " + data.get(d))
    
    print()
    top = input("📋 TOPIC: ")
    return data.get(top,"UP(⬆️)")  


def getKeywords():
    print()
    print("__________________________________")
    keywords = input("🔑 Keyword(s): ")
    return keywords    

def getAuthorAsList():
    returnStr = subprocess.run("git config user.name", capture_output=True, text=True,shell=True)
    return returnStr.stdout.strip()

def getAuthorS():
    print()
    print("__________________________________")
    print("👥 Author(s)")
    returnStr = subprocess.run("git config user.name", capture_output=True, text=True,shell=True)
    print("Default: " + returnStr.stdout)
    print("To use default one, type: d")
    authorS = input("👥 Author(s): ")
    if(authorS == "d"):
        return returnStr.stdout.strip()
    if(authorS.strip() != "" or len(authorS.strip()) == 0):
        return "-"
    return returnStr.stdout.strip()


def getBranchAsList():
    returnStr = subprocess.run("git branch", capture_output=True, text=True,shell=True)
    return returnStr.stdout.strip()

def getWorkingBranch():
    print()
    print("__________________________________")
    print("🔱 BRANCH")
    returnStr = subprocess.run("git branch", capture_output=True, text=True,shell=True)
    print("Default: " + returnStr.stdout)
    print("To use default one, type: d")
    branchOfRepo = input("🔱 BRANCH: ")
    if(branchOfRepo == "d"):
        return returnStr.stdout.strip()
    if(branchOfRepo != "" or len(branchOfRepo.strip()) == 0):
        return "-"    
    return returnStr.stdout.strip()


def getListOfChanges():
    print()
    print("__________________________________")
    listOfChanges = "🗒️ DESCRIPTION OF CHANGES: \n\n"
    print("🗒️ DESCRIPTION OF CHANGES: ")
    print("If you're done, type: r")
    while(True):
        inputItem = input("Item: ")
        if(inputItem == "r"):
            break
        listOfChanges = listOfChanges + "- " + inputItem + "\n"
    return listOfChanges


def getScope():
    
    data = getDataFromJSONConfigFile("commitscope.json")
    
    print()
    print("__________________________________")
    print("🛠️ Scope: \n")
    
    for d in data.keys():
        print(d + " - " + data.get(d))
    print()
    ch = input("🛠️ SCOPE: ")
    return data.get(ch,"GLOBAL 🌐")


def getCurrentDate():
    dateNow = date.today()
    return dateNow.strftime("%B %d, %Y") 


def getCurrentTime():
    timeNow = datetime.now()
    return timeNow.strftime("%H:%M:%S")

def exitScript():
    print("""
        - Stopping...
        - 🔥FireCommit Exited
        """)
    sys.exit()