from tools.nmap import nmap
from tools.ping import ping


def tools():
    print("What do you want to do?")
    try:
        i = input("\t[1]: ping, \n\t[2]: nmap, \n\t[3]: hydra \n")
        if int(i) == 1:
            ping()
        if int(i) == 2:
            nmap()
        if int(i) == 3:
            print("add IP and execute command")
    except ValueError:
        print("invalid input\n")
        tools()
