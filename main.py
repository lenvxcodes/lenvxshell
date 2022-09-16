kebab = False
import pkg_resources
import os
print("Welcome to startup..")
print("Wellcome to DEV release,")
print("I will check if u have installed the modules. else it wont work.")
for package in ['colorama', 'ujson']:
    try:
        dist = pkg_resources.get_distribution(package)
        print('{} ({}) Is installed!'.format(dist.key, dist.version))
    except pkg_resources.DistributionNotFound:
        print('{} Is not installed. OOF.'.format(package))
        a =input("enter = exit()")
        exit()
import colorama
import ujson
def reg():     
        print("So. whats ur username?")
        username =input("user:")
        print(f"Hello {username}!")
        print("so. what password will u set here?")
        password =input("pass:")
        jsons = open("data/data.json", "w")
        dict1 ={"user": username,
            "pass": password,
            "login": "True"}
        ujson.dump(dict1, jsons, indent = 6)
        print("just saved into json file.")
with open("data/data.json", "r") as cfg:
    config: dict = ujson.load(cfg)
if config["login"] == "False":
    reg()
    exit()
print("You are ready to go.")
if config["login"] == "True":
    user = config["user"]
    def terminal():
        kebab = True
        os.system('clear')
        print(f"Wellcome! {user}")
        print("enter your password.")
        passchk =input("pass: ")
        if passchk == config["pass"]:
            print("Wellcome back lenvx!")
            while kebab:
                prefix = f"{user}$~ "
                sytax: str =input(prefix)
                if sytax == 'help':
                    print(f"Commands for {user}:")
                    print("FNX(message)")
                if sytax == "prefix":
                    print(f"current prefix:{prefix}")
                if not sytax.startswith("LNX("):
                    print("Bad value")
                else:
                    print(sytax[4:-1])
        if not passchk == config["pass"]:
            print("Console: Incorrect password.")
terminal()
exit()

