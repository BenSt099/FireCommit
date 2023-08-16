###############################################
################### Imports ###################
###############################################

import os
import sys
import json
import subprocess
from pathlib import Path
from datetime import date
from datetime import datetime


###############################################
################# Functions ###################
###############################################


def get_data_from_json_file(filename):
    with open(filename, "r", encoding="utf-8") as out:
        data = json.load(out)    
    return data

def check_if_git_repo():
    try:
        returnStr = subprocess.run("git status", capture_output=True, text=True,check=True,shell=True)
        returnStr.check_returncode()
    except subprocess.CalledProcessError: 
        return "[x] Couldn't detect git."
    return "[⚬] Detected git."

def template_present():
    filepath = "./msgstruct.json"
    if os.path.isfile(filepath) == False:
        return False, "[x] Couldn't detect msgstruct."
    
    data = get_data_from_json_file(filepath)
    if data["name"] == "default":
        return True, "[i] Loaded default template."
    return True, "[i] Loaded" + data["name"] + "template."


def assemble_commit_message():
    data = get_data_from_json_file("./msgstruct.json")
    msg = ""
    for i in data:
        print("[%s]: %s",i,data[i])
    
    return msg

###############################################
############# Main Functionality ##############
###############################################


def exit_script():
    print("""
        [Command] Stopping...
        🔥FireCommit Exited
        """)
    sys.exit()


def main():
    
    ### Start & Check
    print("🔥FireCommit - V.6.0")
    print("[Check]: %s", check_if_git_repo())
    statusbool,status = template_present()
    if statusbool == False:
        print(status)
        exit_script()
    print("[Check]: %s", status)
    
    ### Assemble commit-message
    
    msg = assemble_commit_message()
    
    
    
    ### Exit
    exit_script()

###############################################
############### Start Script ##################
###############################################

main()