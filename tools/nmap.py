# OS detection -O
# do not ping -PN
# lot of stuff -A
# -p- all ports
def nmap():
    ip = input("enter ip \n")
    params = ""
    os_detection = input("os detection (Y/N)")
    if os_detection == "Y":
        params = params + " -O"
    print("nmap" + params + " " + ip)
