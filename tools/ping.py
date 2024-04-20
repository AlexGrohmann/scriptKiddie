import os

from functions.regex_ip import check_for_valid_ip


def ping():
    ip = input("please add ip: \n")
    if check_for_valid_ip(ip):
        os.system("ping " + ip)
    else:
        ping()
