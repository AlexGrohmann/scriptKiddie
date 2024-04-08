import os


def ping():
    ip = input("please add ip: \n")
    os.system("ping " + ip)
