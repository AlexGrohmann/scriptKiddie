from os import kill
from functions.attack import attack
from functions.backdoor_pdf import backdoor_pdf
from functions.checklist import checklist
from functions.crack import crack
from tools.tools import tools

# alt shift T


def main():
    print("What do you want to do?")
    try:
        i = input(
            "\t[1]: attack, \n\t[2]: backdoor pdf creation, \n\t[3]: crack hash, \n\t[4]: checklist, \n\t[5]: tools \n"
        )
        if i == "exit":
            exit()
        if int(i) == 1:
            attack()
        if int(i) == 2:
            backdoor_pdf()
        if int(i) == 3:
            crack()
        if int(i) == 4:
            checklist()
        if int(i) == 5:
            tools()
    except ValueError:
        print("invalid input\n")
        main()


main()
