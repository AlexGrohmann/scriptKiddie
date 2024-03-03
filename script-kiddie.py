import os
import subprocess


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
    print("crack")


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
