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
        'l': 'LOCAL: 📌',
        'g': 'GLOBAL: 🌐',
        'm': 'MODULE: 🗃️',
       'sm': 'SUBMODULE: 🗄️'
    }
    ch = input("🛠️ Changes (LOCAL (l): 📌, GLOBAL (g): 🌐, MODULE (m): 🗃️, SUBMODULE (sm): 🗄️): ")
    return dictPossibilitiesChanges.get(ch,"GLOBAL: 🌐")

def Keywords():
    keywords = input("🔑⌨️ Keyword(s): ")
    return keywords    

def Topic(inputMsgType):  
    dictPossibilitiesOnionArch = {
        'g': 'GUI: 🖼️',
       'as': 'APPLICATION_SERVICE: 💾',
       'ds': 'DOMAIN_SERVICE: 🪛',
       'dm': 'DOMAIN_MODEL: 🥝',
       'ii': 'INITIAL: 🏹',
        'u': 'UPDATE: ⬆️',
        't': 'TEST: 🛡️',
       'fi': 'FIX: ✅',
        'm': 'MILESTONE: 💎',
        'r': 'RELEASE: 🎆',
        'd': 'DOCUMENTATION: 📓',
        'i': 'INFRASTRUCTURE: 🎛️',
       'do': 'DOCKER: 🐳',
       'sp': 'SPRING: 🌿',
       'gr': 'GRADLE: 🐘'
    }

    dictPossibilitiesLayeredArch = {
        'g': 'GUI: 🖼️',
       'bl': 'BUSINESS_LOGIC: ♟️',
        'p': 'PERSISTENCE: 🧱',
       'ii': 'INITIAL: 🏹',
        'u': 'UPDATE: ⬆️',
        't': 'TEST: 🛡️',
       'fi': 'FIX: ✅',
        'm': 'MILESTONE: 💎',
        'r': 'RELEASE: 🎆',
        'd': 'DOCUMENTATION: 📓',
        'i': 'INFRASTRUCTURE: 🎛️',
       'do': 'DOCKER: 🐳',
       'sp': 'SPRING: 🌿',
       'gr': 'GRADLE: 🐘'
    }

    dictPossibilitiesDefault = {
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
       'gr': 'GRADLE: 🐘'
    }

    if(inputMsgType == "oa"):
        print()
        w = PrettyTable()
        w.field_names = ["(1)","(2)","(3)","(4)"]

        w.add_rows([
            ["GUI: 🖼️ (g)","APPLICATION_SERVICE: 💾 (as)","DOMAIN_SERVICE: 🪛 (ds)","DOMAIN_MODEL: 🥝 (dm)"],
            ["INITIAL: 🏹 (ii)","UPDATE: ⬆️ (u)","TEST: 🛡️ (t)","FIX: ✅ (fi)"],
            ["MILESTONE: 💎 (m)","RELEASE: 🎆 (r)","DOCUMENTATION: 📓 (d)","INFRASTRUCTURE: 🎛️ (i)"],
            ["DOCKER: 🐳 (do)","SPRING: 🌿 (sp)","GRADLE: 🐘 (gr)",""],
        ])

        w.set_style(PLAIN_COLUMNS)
        print("Possible 📋 TOPICS: \n")
        print(w)
        dictPossibilitiesTopics = dictPossibilitiesOnionArch.copy()

    elif(inputMsgType == "la"):
        print()
        z = PrettyTable()
        z.field_names = ["(1)","(2)","(3)","(4)"]

        z.add_rows([
            ["GUI: 🖼️ (g)","BUSINESS_LOGIC: ♟️ (bl)","PERSISTENCE: 🧱 (p)","INITIAL: 🏹 (ii)"],
            ["UPDATE: ⬆️ (u)","TEST: 🛡️ (t)","FIX: ✅ (fi)","MILESTONE: 💎 (m)"],
            ["RELEASE: 🎆 (r)","DOCUMENTATION: 📓 (d)","INFRASTRUCTURE: 🎛️ (i)","DOCKER: 🐳 (do)"],
            ["SPRING: 🌿 (sp)","GRADLE: 🐘","",""]
        ])
        
        z.set_style(PLAIN_COLUMNS)
        print("Possible 📋 TOPICS: \n")
        print(z)
        dictPossibilitiesTopics = dictPossibilitiesLayeredArch.copy()

    else:
        print()
        y = PrettyTable()
        y.field_names = ["(1)","(2)","(3)","(4)"]
       
        y.add_rows([
            ["FIX: ✅ (fi)","WARNING: ⚠️ (w)","FAILED: ❌ (f)","CONTINUOUS_DELIVERY: ♾️ (cd)"],
            ["TEST: 🛡️ (t)","MILESTONE: 💎 (m)","RELEASE: 🎆 (r)","DOCUMENTATION: 📓 (d)"],
            ["LINK: 🔗 (l)","REFACTORING: 🔪 (rf)","GUI: 🖼️ (g)","BUSINESS_LOGIC: ♟️ (bl)"],
            ["ARCHITECTURE: 🏬 (a)","INFRASTRUCTURE: 🎛️ (i)","INITIAL: 🏹 (ii)","UPDATE: ⬆️ (u)"],
            ["PERSISTENCE: 🧱 (p)","APPLICATION_SERVICE: 💾 (as)","DOMAIN_SERVICE: 🪛 (ds)","DOMAIN_MODEL: 🥝 (dm)"],
            ["DOCKER: 🐳 (do)","SPRING: 🌿 (sp)","GRADLE: 🐘",""]
        ])
        y.set_style(PLAIN_COLUMNS)
        print("Possible 📋 TOPICS: \n")
        print(y)
        dictPossibilitiesTopics = dictPossibilitiesDefault.copy()
    
    print()
    top = input("📋 TOPIC: ")
    return dictPossibilitiesTopics.get(top,"UPDATE: ⬆️")  


def startWithMsg():
    x = PrettyTable()
    x.field_names = ["Content","Description"]

    x.add_rows([
             ["👥 AUTHORS",Authors()],
             ["🔑⌨️ KEYWORDS",Keywords()],
             ["🛠️ CHANGES",Changes()],
             ["🔱 BRANCH",Branch()],
             ["🗓️ DATE",Date()],
             ["🕒 TIME",Time()]])
    x.set_style(PLAIN_COLUMNS)

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

    #retCode = subprocess.run(secParam, check=True)
    retCode = subprocess.run(secParam)

    #try:
    #    retCode.check_returncode()
    #except subprocess.CalledProcessError: 
    #    print("❌ Commit - Failure !")
    #    time.sleep(10)
    #    exitProgram()

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
    🔥FireCommit - V.4.8.0
    - Options: op
    - Start:   s
    """)

    checkIfGitRepo()
    inputAction = input("Action: ")

    if(inputAction == "s"):
        print()
        print("""
        | for Layered-Architecture  (la) | 
        | for Onion-Architecture    (oa) | 
        | Custom                     (c) |
        """)
        print()
        commitmsg = input("Type of Commit-Msg: ")
        commitToRepo(Topic(commitmsg),startWithMsg())
        exitProgram()
        
    elif(inputAction == "op"):    
        print("""
        Options:
            - Action:
                    - s: start to assemble a commit message
                    - op: display options
                    - <Enter> quit script

            - Type of Commit-Msg:
                    - Commit Msg for Layered Architecture
                    - Commit Msg for Onion Architecture
                    - Assemble a custom commit message

            - Topics: 
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