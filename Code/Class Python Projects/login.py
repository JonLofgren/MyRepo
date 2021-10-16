import hashlib
from datetime import datetime
import getpass
import os
import time


def timestamp():
    now = datetime.now()
    date = now.strftime("%Y-%m-%d %H:%M:%S")
    return date


def new_user(name):
    while True:
        uName = input("What is your username going to be?\n")
        pass1 = hashlib.md5(getpass.getpass("What is your password going to be: ").encode("UTF-8")).hexdigest()
        pass2 = hashlib.md5(getpass.getpass("Confirm your password: ").encode("UTF-8")).hexdigest()
        if pass1 == pass2:
            with open("shadow.txt", "a") as fShadow:
                fShadow.write(f"{uName} {pass1}\n")
            with open("log.txt", "a") as fLog:
                fLog.write(f"New user: {uName}, created by: {name}, at: {timestamp()}\n")
                break
        else:
            print("Your passwords did not match!")


def login():
    while True:
        unames = []
        shadows = []
        state = False
        while True:
            try:
                with open("shadow.txt", "r") as fShadow:
                    for line in fShadow:
                        separator = line.split()
                        unames.append(separator[0])
                        shadows.append(separator[1])
                break
            except FileNotFoundError:
                os.system("cls" if os.name == "nt" else "clear")
                print("No file found, starting for new user.")
                time.sleep(2)
                new_user("System")
                continue
        while not state:
            print(state, unames, shadows)
            user = input("What is your user name?\n")
            if user in unames:
                count = 0
                position = unames.index(user)
                while count < 3:
                    count += 1
                    passwd = hashlib.md5(getpass.getpass("Please enter your password: ").encode("UTF-8")).hexdigest()
                    if passwd == shadows[position]:
                        state = True
                        break
            else:
                with open("log.txt", "a") as fLog:
                    fLog.write(f"ATTEMPTED LOGIN WITHOUT CREDENTIALS: {timestamp()}")
                    getpass.getpass("Please enter your password: ")
                    getpass.getpass("Please enter your password: ")
                    getpass.getpass("Please enter your password: ")
                    print("Your passwords did not match, exiting program")
                    time.sleep(2)
                    quit()


login()
