from CommitMsg import *
import subprocess


def commitToRepo(inputMsg):

    secParam = "git commit -m \"" + inputMsg + "\""
    print(secParam)
    subprocess.run(secParam)

def main():
    print("""
    🔥FireCommit - V.1.0.0
    - Options: op
    - Start:   st
    - Starting...
    """)

    inputAction = input("Action: ")

    if(inputAction == "st"):
        #print(startWithMsg())
        commitToRepo(startWithMsg())
        
    elif(inputAction == "op"):    
        print("""
        Options:
            - Action: st / op (Start to create a commit message | See Options)
        """)
        main()
    else:
        print("""
        - Stopping...
        - FireCommit Exited (0)
        """)

main()    