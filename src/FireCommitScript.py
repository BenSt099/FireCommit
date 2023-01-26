import sys
import time
import subprocess
from prettytable import PrettyTable
from prettytable import PLAIN_COLUMNS
from datetime import date
from datetime import datetime

def Branch():
    print("🔱 BRANCH")
    returnStr = subprocess.run("git branch", capture_output=True, text=True,shell=True)
    print(returnStr.stdout)
    print("To use default one, type: d")
    branchOfRepo = input("🔱 BRANCH: ")
    if(branchOfRepo == "d"):
        return returnStr.stdout.strip()
    if(branchOfRepo != "" or len(branchOfRepo.strip()) == 0):
        return "-"    
    return returnStr.stdout.strip()

def Date():
    dateNow = date.today()
    return dateNow.strftime("%B %d, %Y") 

def Time():
    timeNow = datetime.now()
    return timeNow.strftime("%H:%M:%S")

def Authors():
    print("👥 Author(s)")
    returnStr = subprocess.run("git config user.name", capture_output=True, text=True,shell=True)
    print(returnStr.stdout)
    print("To use default one, type: d")
    authorS = input("👥 Author(s): ")
    if(authorS == "d"):
        return returnStr.stdout.strip()
    if(authorS.strip() != "" or len(authorS.strip()) == 0):
        return "-"
    return returnStr.stdout.strip()

def ShortListOfChanges():
    listOfChanges = "🗒️ DESCRIPTION OF CHANGES: \n\n"
    print("🗒️ DESCRIPTION OF CHANGES: ")
    print("If you're done, type: r")
    while(True):
        inputItem = input("Item: ")
        if(inputItem == "r"):
            break
        listOfChanges = listOfChanges + "- " + inputItem + "\n"

    return listOfChanges

def Changes():
    dictPossibilitiesChanges = {
        'l': 'LOCAL (📌)',
        'g': 'GLOBAL (🌐)',
        'm': 'MODULE (🗃️)',
       'sm': 'SUBMODULE (🗄️)',
        'r': 'ROOT (🌳)'
    }
    v = PrettyTable()
    v.field_names = ["(1)","(2)"]
    v.add_rows([
        ["LOCAL (l) 📌","GLOBAL (g) 🌐"],
        ["MODULE (m) 🗃️","SUBMODULE (sm) 🗄️"],
        ["ROOT (r) 🌳",""],
    ])
    v.set_style(PLAIN_COLUMNS)
    print("Possible 📋 Scope: \n")
    print(v)
    print()
    ch = input("🛠️ SCOPE: ")
    return dictPossibilitiesChanges.get(ch,"GLOBAL (🌐)")

def Keywords():
    keywords = input("🔑⌨️ Keyword(s): ")
    return keywords    

def Topic():  
    
    dictPossibilitiesTopics = {
       'fi': 'FIX: ✅',
        'w': 'WARNING: ⚠️',
        'f': 'FAILED: ❌',
       'cd': 'CONTINUOUS_DELIVERY: ♾️',
        't': 'TEST: 🛡️',
        'm': 'MILESTONE: 💎',
        'r': 'RELEASE: 🎆',
        'd': 'DOCUMENTATION: 📓',
        'l': 'LINK: 🔗',
       'rf': 'REFACTORING: 🔪',
        'g': 'GUI: 🖼️',
       'bl': 'BUSINESS_LOGIC: ♟️',
       'as': 'APPLICATION_SERVICE: 💾',
       'ds': 'DOMAIN_SERVICE: 🪛',
       'dm': 'DOMAIN_MODEL: 🥝',
        'p': 'PERSISTENCE: 🧱',
        'a': 'ARCHITECTURE: 🏬',
        'i': 'INFRASTRUCTURE: 🎛️',
       'ii': 'INITIAL: 🏹',
       'u' : 'UPDATE: ⬆️',
       'do': 'DOCKER: 🐳',
       'sp': 'SPRING: 🌿',
       'gr': 'GRADLE: 🐘',
       'st': 'STYLE: 🪟',
       'fe': 'FEATURE: 🎉',
       'pe': 'PERFORMANCE: 💯',
       'co': 'CORE: 🌣',
       're': 'REVERT: ♻️'
    }

    print()
    y = PrettyTable()
    y.field_names = ["(1)","(2)","(3)","(4)"]
    
    y.add_rows([
        ["FIX: ✅ (fi)","WARNING: ⚠️ (w)","FAILED: ❌ (f)","CONTINUOUS_DELIVERY: ♾️ (cd)"],
        ["TEST: 🛡️ (t)","MILESTONE: 💎 (m)","RELEASE: 🎆 (r)","DOCUMENTATION: 📓 (d)"],
        ["LINK: 🔗 (l)","REFACTORING: 🔪 (rf)","GUI: 🖼️ (g)","BUSINESS_LOGIC: ♟️ (bl)"],
        ["ARCHITECTURE: 🏬 (a)","INFRASTRUCTURE: 🎛️ (i)","INITIAL: 🏹 (ii)","UPDATE: ⬆️ (u)"],
        ["PERSISTENCE: 🧱 (p)","APPLICATION_SERVICE: 💾 (as)","DOMAIN_SERVICE: 🪛 (ds)","DOMAIN_MODEL: 🥝 (dm)"],
        ["DOCKER: 🐳 (do)","SPRING: 🌿 (sp)","GRADLE: 🐘","STYLE: 🪟 (st)"],
        ["FEATURE: 🎉 (fe)","PERFORMANCE: 💯 (pe)","CORE: 🌣 (co)","REVERT: ♻️ (re)"]
    ])
    y.set_style(PLAIN_COLUMNS)
    print("Possible 📋 TYPES: \n")
    print(y)
    print()
    top = input("📋 TYPE: ")
    return dictPossibilitiesTopics.get(top,"UPDATE: ⬆️")  

def startWithMsg():
    x = PrettyTable()
    x.set_style(PLAIN_COLUMNS)
    x.field_names = ["  Description","Content"]

    x.add_rows([
             ["👥 AUTHORS",Authors()],
             ["🔑⌨️ KEYWORDS",Keywords()],
             ["🛠️ SCOPE",Changes()],
             ["🔱 BRANCH",Branch()],
             ["🗓️ DATE",Date()],
             ["🕒 TIME",Time()]])

    return x.get_string()

def commitToRepo(inputTopic,inputBody):
    print()
    inputMsg = inputTopic + "\n" + inputBody + "\n\n" + ShortListOfChanges()
    print()
    print("___________________________________________")
    print("Commit Message: \n")
    print(inputMsg)
    print()
    print("""
    ⚬ Checking for unstaged commits...
    """)

    print()
    returnStr = subprocess.run("git status", capture_output=True, text=True,check=True,shell=True)

    try:
        returnStr.check_returncode()
    except subprocess.CalledProcessError: 
        print("❌ Checking for unstaged commits failed !")
        print()
        print("⚠️ Committing might not work.")
        print()

    
    if(returnStr.stdout.find("Changes not staged") != -1):
        print("❌ Found Unstaged Commits !")
        print()
        wanttocontinue = input(">>> Want to continue anyway [Y | N] ? ")
        if(wanttocontinue == "N" or wanttocontinue=="n"):
            exitProgram()

    else:
        print("✅ Everything clean !")

    print()
    inputStr = input(">>> Proceed [Y | N] ? ")

    if(inputStr == "N" or inputStr == "n"):
        exitProgram()

    print("⚬ Trying to commit...")
    print()
    secParam = "git commit -m \"" + inputMsg + "\""

    if sys.platform.startswith('win32'):
        retCode = subprocess.run(secParam, check=True) # windows
    elif sys.platform.startswith('linux'):
        retCode = subprocess.run(secParam,shell=True,check=True) # linux
    elif sys.platform.startswith('darwin'):
        retCode = subprocess.run(secParam,shell=True,check=True)

    try:
        retCode.check_returncode()
    except subprocess.CalledProcessError: 
        print("❌ Commit - Failure !")
        time.sleep(10)
        exitProgram()

    print("✅ Commit - Successful !")    
    print()
    runGitPush = input(">>> Run Git Push [Y | N] ? ")
    if(runGitPush == "N" or runGitPush == "n"):
        exitProgram()

    print("⚬ Trying to push...")
    print()
    retCodePush = subprocess.run("git push",check=True,shell=True)

    try:
        retCodePush.check_returncode()
    except subprocess.CalledProcessError: 
        print("❌ Pushing - Failure !")
        time.sleep(5)
        exitProgram()

    print("✅ Pushing - Successful !")

def checkIfGitRepo():
    print()
    print("⚬ Checking if this is a git repository...")
    print()
    returnStr = subprocess.run("git status", capture_output=True, text=True,check=True,shell=True)

    try:
        returnStr.check_returncode()
    except subprocess.CalledProcessError: 
        print("❌ This is not a git repository !")
        time.sleep(5)
        exitProgram()

    print("✅ Everything ok !")
    print()

def exitProgram():
    print("""
        - Stopping...
        - 🔥FireCommit Exited
        """)
    sys.exit()

def main():
    print("""
    🔥FireCommit - V.5
    - Options: op
    - Start:   s
    """)

    checkIfGitRepo()
    inputAction = input("Action: ")

    if(inputAction == "s"):
        print()
        
        commitToRepo(Topic(),startWithMsg())
        exitProgram()
        
    elif(inputAction == "op"):    
        print("""
        Options:
            - Action:
                    - s: start to assemble a commit message
                    - op: display options
                    - <Enter> quit script

            - Type: 
                    - Select a basic topic for the commit
                    - If you can't put it into one word, 
                      your probably take to many steps in
                      one commit.

            - Author(s): 
                    - Name one or more authors
                    - Type d and the script will use the default
                      name that is currently listed in the git 
                      config file.

            - Keyword(s):
                    - Add some keywords to the commit

            - Changes:
                    - Helps you to specify the impact of
                      your commit
                    - Does it effect one file in a package 
                      or the whole project ?
                    - Module / Submodule options: for Gradle
                      Moduls

            - Branch:
                    - Specify the branch where the commit is
                      located

            - Description of Changes:
                    - Specify what the commit is about to do

            - Want to continue anyway [Y | N] ?:
                    - If there are some unstaged commits, you will 
                      receive this notification. If you you still
                      want to commit everything, type: y or Y.       
        """)
        main()
    else:
        exitProgram()

main()    