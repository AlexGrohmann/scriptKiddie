import re


# Class of different styles
class style:
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


def get_ip():
    ip = input("please add ip: \n")
    if re.match("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$", ip):
        return ip
    else:
        print(style.RED, "please insert valid IP\n", style.RESET)
        get_ip()
    return ""
