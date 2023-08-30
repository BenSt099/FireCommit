###############################################
################### Imports ###################
###############################################

import os
import sys
import json
import subprocess
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
    return "[i] Detected git."


def template_present():
    filepath = "./msgstruct.json"
    if os.path.isfile(filepath) == False:
        return False, "[x] Couldn't detect msgstruct."
    
    data = get_data_from_json_file(filepath)
    if data["name"] == "default":
        return True, "[i] Loaded default template."
    return True, "[i] Loaded " + data["name"] + " template."


def config_present():
    filepath = "./config.json"
    if os.path.isfile(filepath) == False:
        return "[x] Couldn't detect config file."
    return "[i] Found config file."


def get_current_date():
    dateNow = date.today()
    return dateNow.strftime("%B %d, %Y") 


def get_current_time():
    timeNow = datetime.now()
    return timeNow.strftime("%H:%M:%S")


def get_modifications():
    returnStr = subprocess.run("git diff --staged --stat", capture_output=True, text=True,shell=True)
    return returnStr.stdout


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
        elif i == "date":
            msg += get_current_date()
        elif i == "time":
            msg += get_current_time()
        elif i == "mods":
            msg += get_modifications()
            print(get_modifications())
        else:
            print("[{}]: ".format(i))
            line = 0
            for j in data[i]:
                print("  ..{}:{}".format(line,j))
                line += 1
            selected = input("[SELECT]: ")
            while int(selected) < 0 or int(selected) >= len(data[i]):
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
    
    ### Start
    print("🔥FireCommit - V.6.2")
    
    ### Set Working Directory
    data = get_data_from_json_file("config.json")
    path_to_project = data["cwd"]
    os.chdir(path_to_project)
    
    ### Checks
    print("[CHECK]: ", config_present())
    statusbool,status = template_present()
    if statusbool == False:
        print(status)
        exit_script()
    print("[CHECK]: ", status)
    print("[CHECK]: ", check_if_git_repo())
    print("[CWD]:   ", os.getcwd())
    
    ### Actions
    print("[OPTION]: 0:start | 1:abort")
    input_option = input("[0|1]: ")
    while input_option != "0" and input_option != "1":
        input_option = input("[0|1]: ")
    
    ### Exit
    if input_option == "1":
        exit_script()
    
    ### Assemble commit-message
    msg = assemble_commit_message()
    print("[OPTION]: 0:show | 1:save | 2:commit | 3:abort.")
    input_option3 = input("[0|1|2|3]: ")
    
    if input_option3 == "0":
        print(msg)
        input_option3 = input("[1|2|3]: ")
    if input_option3 == "3":
        exit_script()
    
    while input_option3 != "1" and input_option3 != "2":
        input_option3 = input("[1|2|3]: ")
        if input_option3 == "3":
            exit_script()
    
    if input_option3 == "0":
        print(msg)
    elif input_option3 == "1":
        save_to_file(msg)
    else:
        check_for_unstaged_files()
        print("[OPTION]: 0:commit | 1:abort.")
        input_option4 = "-1"
        while input_option4 != "0" and input_option4 != "1":
            input_option4 = input("[0|1]: ")
        
        if input_option4 == "1":
            exit_script()
        elif input_option4 == "0":
            commit_to_branch(msg)

    main()

###############################################
############### Start Script ##################
###############################################

main()