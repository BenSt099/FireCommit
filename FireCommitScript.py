from CommitMsg import *
import subprocess
import sys


def commitToRepo(inputMsg):

    inputStr = input("-> Abort(y/n) ? ")

    if(inputStr == "y"):
        exitProgram()

    secParam = "git commit -m \"" + inputMsg + "\""
    print(secParam)
    subprocess.run(secParam)

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
        
    elif(inputAction == "op"):    
        print("""
        Options:
            - Action: st / op (Start to create a commit message | See Options)
        """)
        main()
    else:
        exitProgram()

main()    