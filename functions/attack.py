import subprocess


def attack():
    # read IP
    ip = input("Enter ip:")
    # output IP
    print("Added IP is: " + ip)
    # nmap
    output = subprocess.getoutput("sudo nmap -sS -O " + ip)
    # find in output
    pos1 = output.find("SERVICE")
    pos2 = output.find("Warning:")
    # slice the important news
    print(output[pos1 + 7 : pos2])
    ssh_open = output.find("open  ssh") != -1
    print("SSH is open: ", ssh_open)
    if ssh_open:
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
