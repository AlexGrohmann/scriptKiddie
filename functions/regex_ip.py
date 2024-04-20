import re


def check_for_valid_ip(input):
    return re.match("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$", input)
