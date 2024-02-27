import os
import subprocess

# read IP
ip = input("Enter ip:")
# DEBUG ONLY
ip = "192.168.178.99"
# output IP
print("Added IP is: " + ip)
# nmap
output = subprocess.getoutput("sudo nmap -sS -O " + ip)
# find in output
pos1 = output.find("SERVICE")
pos2 = output.find("Warning:")
# slice the important news
print(output[pos1 + 7 : pos2])
sshOpen = output.find("open  ssh") != -1
print("SSH is open: ", sshOpen)
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
