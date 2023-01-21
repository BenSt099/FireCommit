import subprocess
import sys
from datetime import date
from datetime import datetime





"""
Author(s): 👥
Date: 🗓️, Time: 🕒
Topic: 📋: FIX: ✅, REFACTORING: 🔪, TEST: 🛡️, INITIAL: 🏹, GUI: 🖼️, BUSINESS_LOGIC: ♟️; INFRASTRUCTURE: 🎛️, ARCHITECTURE: 🏬, MILESTONE: 💎, RELEASE: 🎆, DOCUMENTATION: 📓,
LINK: 🔗, CONTINUOUS_DELIVERY: ♾️, WARNING: ⚠️, FAILED: ❌, UPDATE: ⬆️
Keyword(s): 🔑⌨️
Change(s): 🛠️: LOCAL: 📌, GLOBAL: 🌐, MODULE: 🗃️, SUBMODULE: 🗄️
No. of Changes: 🧮
"""



def DateAndTime():
    dateNow = date.today()
    timeNow = datetime.now()
    return "🗓️ DATE: " + dateNow.strftime("%B %d, %Y") + "| 🕒 TIME: " + timeNow.strftime("%H:%M:%S")

def Authors():
    listofAuthors = input("👥 Author(s): ")
    return "👥 AUTHORS: " + listofAuthors

def NoOfChanges():
    no = input("🧮 No. of Changes: ")
    return "🧮 NO. OF CHANGES: " + no

def Changes():
    dictPossibilitiesChanges = {
        'l': 'LOCAL: 📌',
        'g': 'GLOBAL: 🌐',
        'm': 'MODULE: 🗃️',
       'sm': 'SUBMODULE: 🗄️'
    }
    ch = input("🛠️ Changes (LOCAL (l): 📌, GLOBAL (g): 🌐, MODULE (m): 🗃️, SUBMODULE (sm): 🗄️): ")
    return "🛠️ CHANGES: " + dictPossibilitiesChanges.get(ch,"GLOBAL: 🌐")

def Keywords():
    keywords = input("🔑⌨️ Keyword(s): ")
    return "🔑⌨️ KEYWORDS: " + keywords    

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
        'a': 'ARCHITECTURE: 🏬',
        'i': 'INFRASTRUCTURE: 🎛️',
       'ii': 'INITIAL: 🏹',
       'u' : 'UPDATE: ⬆️'
    }

    print("""📋 TOPIC: FIX: ✅ (fi), WARNING: ⚠️ (w), FAILED: ❌ (f), CONTINUOUS_DELIVERY: ♾️ (cd), TEST: 🛡️ (t), MILESTONE: 💎 (m), RELEASE: 🎆 (r),
    DOCUMENTATION: 📓 (d), LINK: 🔗 (l), REFACTORING: 🔪 (rf), GUI: 🖼️ (g), BUSINESS_LOGIC: ♟️ (bl), ARCHITECTURE: 🏬 (a), INFRASTRUCTURE: 🎛️ (i), INITIAL: 🏹 (ii),
    UPDATE: ⬆️ (u)""")
    top = input("📋 TOPIC: ")
    return "📋 TOPIC: " + dictPossibilitiesTopics.get(top,"UPDATE: ⬆️")  

def startWithMsg():
    return "| " + Topic() + " |\n" +  "| " + Authors() + " | " + NoOfChanges() + " | " + Keywords() + " |\n" + "| " + Changes() + " |\n"  + "| " + DateAndTime() + " |\n"
























def commitToRepo(inputMsg):

    inputStr = input(">>> Proceed (Y|N) ? ")

    if(inputStr == "N"):
        exitProgram()

    secParam = "git commit -m \"" + inputMsg + "\""
    #print(secParam)
    subprocess.run(secParam)
    runGitPush = input(">>> Run Git Push (Y|N) ? ")
    if(runGitPush == "N"):
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
    🔥FireCommit - V.1.0.0
    - Options: op
    - Start:   st
    - Starting...
    """)

    inputAction = input("Action: ")

    if(inputAction == "st"):
        commitToRepo(startWithMsg())
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