import os
import subprocess
from time import sleep


# alt shift T
def attack():
    # read IP
    ip = input("Enter ip:")
    # DEBUG ONLY
    ip = "192.168.178.99"
    # output IP
    print("Added IP is: " + ip)
    # nmap
    output = subprocess.getoutput("sudo nmap -sS -O " + ip)
    # find in output
    pos1 = output.find("SERVICE")
    pos2 = output.find("Warning:")
    # slice the important news
    print(output[pos1 + 7 : pos2])
    sshOpen = output.find("open  ssh") != -1
    print("SSH is open: ", sshOpen)
    if sshOpen:
        bruteforce = input("Bruteforce SSH Login? Y/N")
        if bruteforce == "Y":
            print("Lets have some fun")
            # TODO think about Wordlist, rockyou.txt is overkill
            # use cewl
    # dirbuster
    # os.system("gobuster --help")

    # nmap
    #   port 22 open
    #       start simple bruteforce
    #           open connection and execute reverse shell
    # dirbuster
    #   read html and search for inputs
    #   cross-site-scripting
    #   sql injection
    #   look for usernames


def backdoorPDF():
    # https://github.com/Jasmoon99/Embedded-PDF
    print("meow")


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

    result = subprocess.run(["ls"], shell=True, capture_output=True, text=True)
    print("XXXXXXXXX")
    print(result)
    print(result.stdout)

    p = subprocess.Popen(["hash-identifier", hash], stdout=subprocess.PIPE)
    print(str(p.stdout))
    p.kill()
    print("killed")


def main():
    print("What do you want to do?")
    try:
        i = input(
            "\t[1]: attack, \n\t[2]: backdoor pdf creation, \n\t[3]: crack hash \n"
        )
        if int(i) == 1:
            attack()
        if int(i) == 2:
            backdoorPDF()
        if int(i) == 3:
            crack()
    except ValueError:
        print("invalid input\n")
        main()


main()
