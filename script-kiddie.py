import os
import re
import subprocess
import time
import paramiko


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
            print_status("IP added: " + ip)
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

    # TODO: SMB
    # TODO: SQLmap
    # TODO: FTP

    if ssh_open:
        bruteforce = input("Bruteforce SSH Login? Y/N: ")
        if bruteforce.upper() == "Y":
            print("Let's have some fun")
            # TODO: Think about Wordlist, rockyou.txt is overkill
            # Use cewl
        # SSH connection details

        # use values from bruteforce
        hostname = "your_hostname"
        port = 22
        username = "your_username"
        password = "your_password"
        command = "ls -l"  # Example command to execute

        # Establish SSH connection
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        try:
            ssh.connect(hostname, port, username, password)
            print("SSH connection established successfully.")

            # Execute command
            stdin, stdout, stderr = ssh.exec_command(command)

            # Read the output
            output = stdout.read().decode()
            error = stderr.read().decode()

            if output:
                print("Command output:")
                print(output)
            if error:
                print("Error:")
                print(error)

        finally:
            # Close the SSH connection
            ssh.close()


def backdoor_pdf():
    print("meow")


def checklist():
    print(
        "Return a path for Yes and no question to do a checklist for pentest (return commands and todos)"
    )


def crack():

    # Command to run name-that-hash
    command = ["name-that-hash", "--text", "1e6681065a0ddfa80714a3df70438f12"]

    # Start the process and capture its output
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Read the output
    output, _ = process.communicate()
    output = output.decode()

    # Check if the process completed successfully
    if process.returncode == 0:

        # Regular expression to extract any hash type mentioned after "Most Likely"
        pattern = r"Most Likely\s+(\w+)"

        # Search for the pattern in the output
        match = re.search(pattern, output)

        # If the pattern is found, extract the hash type
        if match:
            hash_type = match.group(1)
            print("Hash type:", hash_type)
        else:
            print("Hash type not found.")
    else:
        print("Error running name-that-hash:", process.stderr.read().decode().strip()) # type: ignore


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
        # TODO: John
        # TODO: Reverse shells
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

# meow