import os
import subprocess
from time import sleep

from functions.attack import attack
from functions.backdoorPDF import backdoor_pdf
from tools.ping import ping


# alt shift T


def crack():
    # hashidentifier
    # john
    # etc.
    # input(hash)
    # demo hash 1e6681065a0ddfa80714a3df70438f12 md5
    # demo hash 0400774cdcab43bc634ae6e5d737e9b6c7c8e5e3 sha1
    hash = input("please add hash to crack: ")
    # demo
    hash = "1e6681065a0ddfa80714a3df70438f12"
    # hash-identifier
    print("For debugging it uses this hash: " + hash)

    # result = subprocess.run(["ls"], shell=True, capture_output=True, text=True)
    # print("XXXXXXXXX")
    # print(result)
    # print(result.stdout)

    p = subprocess.Popen(
        ["hash-identifier", hash],
        shell=True,
        text=True,
        stderr=subprocess.PIPE,
        stdout=subprocess.PIPE,
    )
    stdout, stderr = p.communicate()

    print(stdout)


def checklist():
    print(
        "Return a path for Yes and no question to do a checklist for pentest (return commands and todos)"
    )


def tools():
    print("What do you want to do?")
    try:
        i = input("\t[1]: ping, \n\t[2]: nmap, \n\t[3]: hydra \n")
        if int(i) == 1:
            ping()
        if int(i) == 2:
            print("add IP and execute command")
        if int(i) == 3:
            print("add IP and execute command")
    except ValueError:
        print("invalid input\n")
        main()


def main():
    print("What do you want to do?")
    try:
        i = input(
            "\t[1]: attack, \n\t[2]: backdoor pdf creation, \n\t[3]: crack hash, \n\t[4]: checklist, \n\t[5]: tools \n"
        )
        if int(i) == 1:
            attack()
        if int(i) == 2:
            backdoor_pdf()
        if int(i) == 3:
            crack()
        if int(i) == 4:
            checklist()
        if int(i) == 5:
            tools()
    except ValueError:
        print("invalid input\n")
        main()


main()
