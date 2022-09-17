#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Lev shell"""
rst = 0

kebab = False
import os
import readline
import getpass
LNX_sys = os.system
from atexit import register as fn_register
from datetime import date

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
print("I will check if u have installed the modules. else it
for package in ["colorama", "ujson"]:
    try:
        dist = pkg_resources.get_distribution(package)
        print("{} ({}) Is installed!".format(dist.key, dist.
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
    dict1 = {"user": username, "pass": password, "login": "T
    ujson.dump(dict1, jsons, indent=6)
    print("just saved into json file.")


with open("data/data.json", "r") as cfg:
    config: dict = ujson.load(cfg)
if config["login"] == "False":
    reg()
    exit()
# main part so i dont lose it.
print("You are ready to go.")
if config["login"] == "True":
    user = config["user"]
    prefix = config["prefix"]
    def Confirmation(com):
        print("Confirmation")
        passconfirm =getpass.getpass(f"Pass for {user}, {com
        if passconfirm == config["pass"]:
            rst = 0
            pass
        if not passconfirm == config["pass"]:
            print("Try again.")
            if rst == 3:
                print("INFl")
                rst = 0
                pass
            rst = rst + 1
            return Confirmation()
    def terminal():
        kebab = True
        print(f"Wellcome! {user}")
        print("enter your password.")
        passchk = getpass.getpass("pass: ")
        if passchk == config["pass"]:
            os.system("clear")
            print("Wellcome back lenvx!")
            today = date.today()
            d1 = today.strftime("%d/%m/%Y")
            print(d1)
            print("------------------------------------")
            while kebab:
                sytax: str = input(prefix.replace("{user}", 
                if sytax == "help":
                    print(f"Commands for {user}:")
                    print("FNX(message)")
                    print("CNGprefix >> changes prefix")
                    print("resLNX >> restarts script.")
                    print("clrhy >> clears history")
                    print("credits")
                    print("LNXkill >> exits the terminal.")
                elif sytax == "CNGprefix":
                    print(f"current prefix:{prefix}")
                    prefixe = input("prefix:")
                    config["key"] = "value"
                    with open("data/data.json", "w") as cfgf
                        ujson.dump(config, cfgf, indent=4)
                elif sytax.startswith("LNX("):
                    print(sytax[4:-1])
                elif sytax == "resLNX":
                    print("restarting script...")
                    os.system("clear && python main.py")
                    return
                elif sytax == "credits":
                    print("very big credit to @TruncatedDino
                elif sytax == "clrhy":
                    print("cleaned the history..")
                    his = open(HISTORY_FILE, "w").close()
                elif not sytax.strip():
                    pass
                if sytax == "LNXkill":
                    print("Exiting...")
                    exit()
                if sytax == "LNXpass":
                    Confirmation('LnxPass')
                    
                else:
                    print("Oof.")
        if not passchk == config["pass"]:
            print("Console: Incorrect password.")
            print("Reloading...")
            return terminal(), LNX_sys('clear')
terminal()
exit()
                else:
                    print("Oof.")
        if not passchk == config["pass"]:
            print("Console: Incorrect password.")
            print("Reloading...")
            return terminal(), LNX_sys('clear')

terminal()
exit()
