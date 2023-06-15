###############################################
################### Imports ###################
###############################################


import sys
from pathlib import Path
from datetime import date
from datetime import datetime
from funcs import *


###############################################
############# Main Functionality ##############
###############################################


def exitScript():
    print("""
        - Stopping...
        - 🔥FireCommit Exited
        """)
    sys.exit()


def main():
    print("""
    🔥FireCommit - V.6.0
    - Options:  op
    - Start:    s
    - Pre-Push: pp
    """)

    checkIfCurrentDirIsGitRepo()
    inputAction = input("Action: ")
    if inputAction == "s":
        print()
        runGitCommit(assembleCommitMSGFromFile())
        runGitPush()
        exitScript()
    elif inputAction == "pp":    
        print()
        inputop = input("Activate Hook [pre-push] ? ")
        if inputop == "N" or inputop == "n":
            exitScript()
        print()
        comm = input("Run Command before push: ")    
        retcode = createPrePushHook(comm)
        if retcode != 0:
            print("❌ Activation of hook failed.")
        print("✅ Activation of hook successful.")
    elif inputAction == "op":    
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

            - Scope:
                    - Helps you to specify the impact of
                      your commit
                    - Does it effect one file in a package 
                      or the whole project ?
                    - Module / Submodule options: for Gradle
                      Moduls
                    - Options for Onion / Layered Architecture

            - Branch:
                    - Specify the branch where the commit is
                      located

            - Description of Changes:
                    - Specify what the commit is about to do     
        """)
        main()
    else:
        exitScript()


###############################################
############### Start Script ##################
###############################################

main()    