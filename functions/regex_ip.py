import re


def get_ip():
    ip = input("please add ip: \n")
    if re.match("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$", ip):
        return ip
    else:
        print("please insert valid IP\n")
        get_ip()
    return ""
