import os
import re
import subprocess


class Colors:
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    UNDERLINE = "\033[4m"
    RESET = "\033[0m"


def print_error(error):
    print(f"{Colors.RED}{error}{Colors.RESET}")


def print_status(status):
    print(f"{Colors.GREEN}{status}{Colors.RESET}")


def get_ip():
    while True:
        ip = input("Please enter an IP address: \n")
        if re.match("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$", ip):
            print_status("IP added: {ip}")
            return ip
        else:
            print_error("Please enter valid input")


def attack():
    ip = input("Enter IP address: ")
    print(f"Entered IP address is: {ip}")

    nmap_output = subprocess.getoutput(f"sudo nmap -sS -O {ip}")

    pos1 = nmap_output.find("SERVICE")
    pos2 = nmap_output.find("Warning:")

    print(nmap_output[pos1 + 7 : pos2])

    ssh_open = "open  ssh" in nmap_output
    print("SSH is open: ", ssh_open)

    if ssh_open:
        bruteforce = input("Bruteforce SSH Login? Y/N: ")
        if bruteforce.upper() == "Y":
            print("Let's have some fun")
            # TODO: Think about Wordlist, rockyou.txt is overkill
            # Use cewl


def backdoor_pdf():
    print("meow")


def checklist():
    print(
        "Return a path for Yes and no question to do a checklist for pentest (return commands and todos)"
    )


def crack():
    hash = input("Please add hash to crack: ")
    hash = "1e6681065a0ddfa80714a3df70438f12"
    print(f"For debugging it uses this hash: {hash}")

    p = subprocess.Popen(
        ["hash-identifier", hash],
        shell=True,
        text=True,
        stderr=subprocess.PIPE,
        stdout=subprocess.PIPE,
    )
    stdout, _ = p.communicate()
    print(stdout)


def gobuster():
    ip = input("Enter IP: ")
    wordlist = input("Wordlist (S/M/L): ")
    if wordlist.upper() == "S":
        wordlist = "./small-word-list.txt"
    elif wordlist.upper() == "M":
        wordlist = "./medium-word-list.txt"
    elif wordlist.upper() == "L":
        wordlist = "./large-word-list.txt"
    os.system(f"gobuster dir -u {ip} -w {wordlist}")


def nmap():
    ip = input("Enter IP: ")
    os_detection = input("OS detection (Y/N): ")
    params = "-O" if os_detection.upper() == "Y" else ""
    os.system(f"nmap {params} {ip}")


def ping():
    os.system(f"ping {get_ip()}")


def tools():
    print("What do you want to do?")
    try:
        i = int(input("\t[1]: Ping\n\t[2]: Nmap\n\t[3]: Gobuster\n"))
        if i == 1:
            ping()
        elif i == 2:
            nmap()
        elif i == 3:
            gobuster()
        else:
            print("Invalid input\n")
            tools()
    except ValueError:
        print("Invalid input\n")
        tools()


def main():
    print("What do you want to do?")
    try:
        i = int(
            input(
                "\t[1]: Attack\n\t[2]: Backdoor PDF creation\n\t[3]: Crack hash\n\t[4]: Checklist\n\t[5]: Tools\n"
            )
        )
        if i == 1:
            attack()
        elif i == 2:
            backdoor_pdf()
        elif i == 3:
            crack()
        elif i == 4:
            checklist()
        elif i == 5:
            tools()
        else:
            print("Invalid input\n")
            main()
    except ValueError:
        print("Invalid input\n")
        main()


main()
