import os

# read IP
ip = input("Enter ip:")
# output IP
print("Added IP is: " + ip)
# nmap
os.system("nmap -h")
# dirbuster
os.system("gobuster --help")

# nmap
#   port 22 open
#       start simple bruteforce
#           open connection and execute reverse shell
# dirbuster
#   read html and search for inputs
#   cross-site-scripting
#   sql injection
#   look for usernames
