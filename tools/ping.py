import os

from functions.regex_ip import get_ip


def ping():
    os.system("ping " + get_ip())
