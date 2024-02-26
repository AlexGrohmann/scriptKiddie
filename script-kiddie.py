import os
import subprocess

# read IP
ip = input("Enter ip:")
# output IP
print("Added IP is: " + ip)
# nmap
output = subprocess.getoutput("nmap -h")
# find in output
pos1 = output.find("Nmap")
# slice the important news
print(output[pos1 : pos1 + 9])
# dirbuster
# os.system("gobuster --help")

# nmap
#   port 22 open
#       start simple bruteforce
#           open connection and execute reverse shell
# dirbuster
#   read html and search for inputs
#   cross-site-scripting
#   sql injection
#   look for usernames
