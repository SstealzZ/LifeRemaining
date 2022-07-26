import utils

def help():
    print("First args: The gender use -m or -f")
    print("Second args: Your date of birth, use this format dd/mm/yy")
    print("Experimental function, Third args: Graphical args")

def chech_date(date):
    i = 0
    while (i < len(date)):
        if(i == 3 and i == 6):
            if (date[i] != '/'):
                print("Bad Date")
                exit(84)
            i += 1
        else:
            utils.get_number(1)
            i += 1
        