import os


# gobuster dir -u http://$IP -w ./wordlist.txt
def gobuster():
    ip = input("enter ip \n")
    wordlist = input("wordlist (S/M/L)")
    if wordlist == "S":
        wordlist = "./small-word-list.txt"
    if wordlist == "M":
        wordlist = "./medium-word-list.txt"
    if wordlist == "L":
        wordlist = "./large-word-list.txt"
    # os.system("gobuster dir -u " + ip + " -w " + wordlist)
    print("gobuster dir -u " + ip + " -w " + wordlist)
