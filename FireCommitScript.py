import os
import sys
import subprocess
from tabulate import tabulate
from datetime import date
from datetime import datetime

def Branch():
    print("🔱 BRANCH")
    print(os.popen("git branch").read())
    retOS = os.popen("git branch").read()
    print("To use default one, type: d")
    branchOfRepo = input("🔱 BRANCH: ")
    if(branchOfRepo == "d"):
        return retOS.strip()
    return branchOfRepo

def Date():
    dateNow = date.today()
    return dateNow.strftime("%B %d, %Y") 

def Time():
    timeNow = datetime.now()
    return timeNow.strftime("%H:%M:%S")

def Authors():
    
    listofAuthors = input("👥 Author(s): ")
    return listofAuthors

def NoOfChanges():
    no = input("🧮 No. of Changes: ")
    return no

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
        'i': 'INFRASTRUCTURE: 🎛️'
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
        'i': 'INFRASTRUCTURE: 🎛️'
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
       'u' : 'UPDATE: ⬆️'
    }

    if(inputMsgType == "oa"):
        print()
        print("""
        Possible 📋 TOPICS:

        | GUI: 🖼️ (g)       | APPLICATION_SERVICE: 💾 (as) | DOMAIN_SERVICE: 🪛 (ds) | DOMAIN_MODEL: 🥝 (dm)  |
        | INITIAL: 🏹 (ii)  | UPDATE: ⬆️ (u)               | TEST: 🛡️ (t)            | FIX: ✅ (fi)           |
        | MILESTONE: 💎 (m) | RELEASE: 🎆 (r)              | DOCUMENTATION: 📓 (d)   | INFRASTRUCTURE: 🎛️ (i) |
        """)
        dictPossibilitiesTopics = dictPossibilitiesOnionArch.copy()

    elif(inputMsgType == "la"):
        print()
        print("""
        Possible 📋 TOPICS:
        
        | GUI: 🖼️ (g)     | BUSINESS_LOGIC: ♟️ (bl) | PERSISTENCE: 🧱 (p)    | INITIAL: 🏹 (ii)  |
        | UPDATE: ⬆️ (u)  | TEST: 🛡️ (t)            | FIX: ✅ (fi)           | MILESTONE: 💎 (m) |
        | RELEASE: 🎆 (r) | DOCUMENTATION: 📓 (d)   | INFRASTRUCTURE: 🎛️ (i) |
        """)
        dictPossibilitiesTopics = dictPossibilitiesLayeredArch.copy()

    else:
        print()
        print("""
        Possible 📋 TOPICS:

        | FIX: ✅ (fi)         | WARNING: ⚠️ (w)              | FAILED: ❌ (f)          | CONTINUOUS_DELIVERY: ♾️ (cd) |
        | TEST: 🛡️ (t)         | MILESTONE: 💎 (m)            | RELEASE: 🎆 (r)         | DOCUMENTATION: 📓 (d)        |
        | LINK: 🔗 (l)         | REFACTORING: 🔪 (rf)         | GUI: 🖼️ (g)             | BUSINESS_LOGIC: ♟️ (bl)      |  
        | ARCHITECTURE: 🏬 (a) | INFRASTRUCTURE: 🎛️ (i)       | INITIAL: 🏹 (ii)        | UPDATE: ⬆️ (u)               |   
        | PERSISTENCE: 🧱 (p)  | APPLICATION_SERVICE: 💾 (as) | DOMAIN_SERVICE: 🪛 (ds) | DOMAIN_MODEL: 🥝 (dm)        |  
        """)
        dictPossibilitiesTopics = dictPossibilitiesDefault.copy()
    
    print()
    top = input("📋 TOPIC: ")
    return dictPossibilitiesTopics.get(top,"UPDATE: ⬆️")  


def startWithMsg(topic):

    table = [[Topic(topic),""],
             ["",""],
             ["👥 AUTHORS",Authors()],
             ["🧮 NO. OF CHANGES",NoOfChanges()],
             ["🔑⌨️ KEYWORDS",Keywords()],
             ["🛠️ CHANGES",Changes()],
             ["🔱 BRANCH",Branch()],
             ["🗓️ DATE",Date()],
             ["🕒 TIME",Time()]]

    #print(tabulate(table, tablefmt='grid'))
    
    # return "| " + Topic(topic) + " |\n" +  "| " + Authors() + " | " + NoOfChanges() + " | " + Keywords() + " |\n" + "| " + Changes() + " | " + Branch() +  " |\n"  + "| " + DateAndTime() + " |\n"
    return tabulate(table, tablefmt='grid')

def commitToRepo(inputMsg):
    print()
    
    print("Commit Message: \n")
    print(inputMsg)
    print()
    inputStr = input(">>> Proceed (Y|N) ? ")

    if(inputStr == "N" or inputStr == "n"):
        exitProgram()
    secParam = "git commit -m \"" + inputMsg + "\""
    subprocess.run(secParam)
    print()
    runGitPush = input(">>> Run Git Push (Y|N) ? ")
    if(runGitPush == "N" or runGitPush == "n"):
        exitProgram()
    subprocess.run("git push")

def exitProgram():
    print("""
        - Stopping...
        - FireCommit Exited (0)
        """)
    sys.exit()

def main():
    print("""
    🔥FireCommit - V.2.0.0
    - Options: op
    - Start:   st
    - Starting...
    """)
    
    inputAction = input("Action: ")

    if(inputAction == "st"):
        print()
        print("""
        | Layered-Architecture  (la) | 
        | Onion-Architecture    (oa) | 
        | Custom                 (c) |
        """)
        print()
        commitmsg = input("Type of Commit-Msg: ")
        commitToRepo(startWithMsg(commitmsg))
        exitProgram()
        
    elif(inputAction == "op"):    
        print("""
        Options:
            - Action: st / op (Start to create a commit message | See Options)
        """)
        main()
    else:
        exitProgram()

main()    