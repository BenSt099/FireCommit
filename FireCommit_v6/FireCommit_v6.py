###############################################
################### Imports ###################
###############################################

import os
import sys
import json
import subprocess


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
        return "Couldn't detect git."
    return "Detected git."


def template_present():
    filepath = "./msgstruct.json"
    if os.path.isfile(filepath) == False:
        return False, "[x] Couldn't detect msgstruct."
    
    data = get_data_from_json_file(filepath)
    if data["name"] == "default":
        return True, "Loaded default template."
    return True, "Loaded" + data["name"] + "template."


def assemble_commit_message():
    data = get_data_from_json_file("./msgstruct.json")
    msg = ""
    for i in data:
        if i == "name":
            continue
        elif i.startswith('blank'):
            msg += "\n"
        elif data[i] == "input":
            msg += input("[INPUT]: ")
        elif i.startswith('Seperator'):
            msg += data[i]
        else:
            print("[{}]: {}".format(i, data[i]))
            selected = input("[SELECT]: ")
            msg += data[i][int(selected)]
    return msg


def save_to_file(msg):
    with open("commit-msg.txt", "w", encoding="utf-8") as outputFile:
        outputFile.write(msg)
    print("[LOG]: Saved to file 'commit-msg.txt'.")


def check_for_unstaged_files():
    try:
        returnStr = subprocess.run("git status", capture_output=True, text=True,check=True,shell=True)
        returnStr.check_returncode()
    except subprocess.CalledProcessError: 
        print("[x]: Checking for unstaged files failed.")

    if(returnStr.stdout.find("Changes not staged") != -1):
        print("[i]: Found unstaged files.")
    else:
        print("[i]: Everything Clean.")


def commit_to_branch(msg):
    print("[i]: Trying to commit.")
    secParam = "git commit -m \"" + msg + "\""

    if sys.platform.startswith('win32'):
        try:
            retCode = subprocess.run(secParam, check=True) # windows
        except subprocess.CalledProcessError:
            print("[x]: Failed to commit.")
    elif sys.platform.startswith('linux'):
        try:
            retCode = subprocess.run(secParam,shell=True,check=True) # linux
        except subprocess.CalledProcessError:
            print("[x]: Failed to commit.")
    elif sys.platform.startswith('darwin'):
        try:
            retCode = subprocess.run(secParam,shell=True,check=True)
        except subprocess.CalledProcessError:
            print("[x]: Failed to commit.")

    try:
        retCode.check_returncode()
    except subprocess.CalledProcessError: 
        print("[x]: Failed to commit.")
    print("[i]: Successfully committed.") 


###############################################
############# Main Functionality ##############
###############################################


def exit_script():
    print("[LOG]: Stopping...")
    print("🔥FireCommit Exited")
    sys.exit()


def main():
    
    ### Start & Check
    print("🔥FireCommit - V.6.0")
    print("[CHECK]: ", check_if_git_repo())
    statusbool,status = template_present()
    if statusbool == False:
        print(status)
        exit_script()
    print("[CHECK]: ", status)
    
    ### Exit
    print("[OPTION]: Start, abort.")
    input_option = input("[S|A]: ")
    if input_option == "A" or input_option == "a":
        exit_script()
    
    ### Assemble commit-message
    
    msg = assemble_commit_message()
    print("[OPTION]: Save to file and not commit?")
    input_option2 = input("[Y|N]: ")
    if input_option2 == "Y" or input_option2 == "y":
        save_to_file(msg)
    else:
        check_for_unstaged_files()
        commit_to_branch(msg)
    main()

###############################################
############### Start Script ##################
###############################################

main()