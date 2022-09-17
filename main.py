#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Lev shell"""
CUM = 0
GLOR = False
secGLOR = GLOR
kebab = False
import platform
import os
import readline
import getpass
import platform
import time
LNX_sys = os.system
from atexit import register as fn_register
from datetime import date
today = date.today()
d1 = today.strftime("%d/%m/%Y")

HISTORY_FILE: str = "sh_history"

if not os.path.isfile(HISTORY_FILE):
    open(HISTORY_FILE, "w").close()

readline.parse_and_bind("tab: complete")

fn_register(readline.write_history_file, HISTORY_FILE)
fn_register(readline.read_history_file, HISTORY_FILE)

readline.read_history_file(HISTORY_FILE)
readline.set_history_length(5000)
from copy import deepcopy

import pkg_resources

print("Welcome to startup..")
print("Wellcome to DEV release,")
print("I will check if u have installed the modules. else it wont work.")
for package in ["colorama", "ujson"]:
    try:
        dist = pkg_resources.get_distribution(package)
        print("{} ({}) Is installed!".format(dist.key, dist.version))
    except pkg_resources.DistributionNotFound:
        print("{} Is not installed. OOF.".format(package))
        a = input("enter = exit()")
        exit()
import colorama
import ujson


def reg():
    print("So. whats ur username?")
    username = input("user:")
    print(f"Hello {username}!")
    print("so. what password will u set here?")
    password = input("pass:")
    jsons = open("data/data.json", "w")
    dict1 = {"user": username, "pass": password, "login": "True", "prefix": f"{user}$~"}
    ujson.dump(dict1, jsons, indent=6)
    print("just saved into json file.")


with open("data/data.json", "r") as cfg:
    config: dict = ujson.load(cfg)
if config["login"] == "False":
    reg()
    exit()
# main part so i dont lose it.
print("You are ready to go.")
from colorama import Fore
if config["login"] == "True":
    user = config["user"]
    prefix = config["prefix"]
    def fetch():
        print(f"""{Fore.GREEN}
                       %%%%%%%%%
                 %%%%%%%%%%%%%%%%%%%%%%%
             &%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
           %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&
         %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%             {Fore.RED}OS      = {Fore.RESET}{platform.system()}{Fore.GREEN}
       %%%%%%%%%%%%%%%   %%%%%%.  %%%%%%%%%%%%%%%%            {Fore.RED}Date    = {Fore.RESET}{d1}{Fore.GREEN}
      %%%%%%%%%%%%%%#  *%%%%%%   %%%%%%%%%%%%%%%%%%&          {Fore.RED}RP      = {Fore.RESET}LenvxREPL{Fore.GREEN}
     %%%%%%%%%%%%%%#     *%%%,  %%%%%%%%%%%%%%%%%%%%          {Fore.RED}State   = {Fore.RESET}DEV{Fore.GREEN}
    %%%%%%%%%%%%%%%   %%%#     %%%%%%%%%%%%%%%%%%%%%%         {Fore.RED}support = {Fore.RESET}BASH{Fore.GREEN}
    %%%%%%%%%%%%%%%  ,%%%%%*  #.   /%%%%%%%%%%%%%%%%%
    %%%%%%%%%%%%%%%  *%%%%/  *    ,#%%%%%%%%%%%%%%%%%
    %%%%%%%%%%%%%%%  .%(.    (%%%%%%%%%%%%%%%%%%%%%%%
     %%%%%%%%%%%%%%,   ,%  /%%%%%%%%%%%%%%%%%%%%%%%%%
     &%%%%%%%%%%%%%%   #  /%%%%%%%%%%%%%%%%%%%%%%%%%
       %%%%%%%%%%%%%%   %%%%%%%%%%%%%%%%%%%%%%%%%%%
        %%%%%%%%%%%%%%#  /%%%%%%%%%%%%%%%%%%%%%%%&
         %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%&
           &%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
                &%%%%%%%%%%%%%%%%%%%%%%%%%&
                    %%%%%%%%%%%%%%%
        {Fore.RESET} """)
    def Confirmation(com):
        print("Confirmation")
        passconfirm =getpass.getpass(f"Pass for {user}, {com}: ")
        if passconfirm == config["pass"]:
            CUM = True
            pass
        if not passconfirm == config["pass"]:
            CUM = False
            pass
    def login():
        print(f"Registered as {user}.")
        print(f"Wellcome! {user}")
        print("enter your password.")
        passchk = getpass.getpass("pass:")
        if passchk == config["pass"]:
            terminal()
        if not passchk == config["pass"]:
            print(f"{Fore.RED}Console{Fore.RESET}: {Fore.RED}Incorrect {Fore.BLUE}password{Fore.RESET}")
            print(f"{Fore.MAGENTA} Reloading{Fore.RESET}...")
            return login(), LNX_sys('clear')
    def terminal():
        if 1 == 1:
            kebab = True
            print(f"{Fore.MAGENTA}Wellcome back {Fore.BLUE}lenvx!")
            print(Fore.LIGHTBLACK_EX + d1)
            print(f"{Fore.RED}------{Fore.YELLOW}------------{Fore.BLUE}----------------{Fore.RESET}")
            while kebab:
                #syntax 
                sytax: str = input(prefix.replace("{user}", config["user"]))
                #Commands
                if sytax == "help":
                    print(f"Commands for {Fore.YELLOW + user + Fore.RESET}:")
                    print(f"{Fore.BLUE} FNX{Fore.GREEN}(message)")
                    print(f"{Fore.BLUE}CNGprefix >> {Fore.GREEN}changes prefix")
                    print(f"{Fore.BLUE}resLNX -h >> {Fore.GREEN}Help list of restarting LNXSCRIPT.")
                    print(f"{Fore.BLUE}clrhy >> {Fore.GREEN}clears history")
                    print(f"{Fore.BLUE}credits")
                    print(f"{Fore.BLUE}LNXkill{Fore.GREEN} >> exits the terminal.")
                    print(f"{Fore.BLUE}LenFetch{Fore.GREEN} >> Dev Fetch..")
                    print(f"{Fore.BLUE}FNXpass{Fore.GREEN} >> change password..")
                    print(f"?Update - whats new?")
                    print(f"LNXver")
                    print("ADDED - FNX as admin. in progress!")
                    print(Fore.RESET)
                elif sytax == "CNGprefix":
                    print(f"current prefix:{prefix}")
                    prefixe = input("prefix:")
                    config["prefix"] = prefixe
                    with open("data/data.json", "w") as cfgf:
                        ujson.dump(config, cfgf, indent=4)
                elif sytax.startswith("LNX("):
                    print(sytax[4:-1])
                elif sytax == "resLNX":
                    print("restarting script...")
                    os.system("clear && python main.py")
                    return
                elif sytax == "credits":
                    print("very big credit to @TruncatedDinosour on github (ari)")
                elif sytax == "clrhy":
                    print("cleaned the history..")
                    his = open(HISTORY_FILE, "w").close()
                elif not sytax.strip():
                    pass
                elif sytax == "LNXkill":
                    print("Exiting...")
                    exit()
                elif sytax == "FNXpass":
                    Confirmation('LnxPass')
                    if CUM == False:
                        print("Invalid PASS for LNXPASS!")
                    if CUM == True:
                        print("Change pass")
                    newpass=input("New pass: ")
                    nepass=input("ConfirmLNX: ")
                    if newpass == nepas:
                        config["pass"] = newpass
                    with open("data/data.json", "w") as cfgf:
                        ujson.dump(config, cfgf, indent=4)
                    if not newpass == nepas:
                        print("Try again. Sorry.")
                elif sytax == "pass":
                    print("FNX: No admin.")
                elif sytax == "LNXpass":
                    print("LNX: FNX REQUEST,.")
                elif sytax == "LenFetch":
                    fetch() 
                elif sytax == "resLNX -falselogin":
                    print("Redirecting to Repl-LENVX-DEV")
                    time.sleep(2)
                    return terminal()
                elif sytax == "resLNX -h":
                    print(f"{Fore.LIGHTBLUE_EX} resLNX - {Fore.RED} restarts script.")
                    print(f"{Fore.LIGHTBLUE_EX} resLNX -falselogin - {Fore.RED} restarts terminal.")
                elif sytax == "?update":
                    print("new commands.")
                    print("bugs fixed!")
                elif sytax == "LNXver"
                print("DEV.0.1")
                else:
                    print("Oof.")
login()
