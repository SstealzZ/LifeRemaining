from my_colors import my_colors
import calculate

def get_print_free():
    return (my_colors.White + ".")

def get_print_resp():
    return (my_colors.LightBlue + ".")

def get_print_old():
    return(my_colors.LightYellow + ".")

def get_print_crit():
    return(my_colors.LightRed + ".")

def get_print_use():
    return (my_colors.LightGreen + "*")

def gui(opt, value):
    i = 0
    j = 0
    tot = 0
    test = calculate.get_years_alive(value) + calculate.get_years_remaining(opt, value) + 1

    while (j != test):
        while(i != 52):
            if (tot <= calculate.get_weeks_alive(value)):
                print(get_print_use(), end='')
                i += 1
                tot += 1
            else:
                if(j >= 30 and j <= test - 25):
                    print(get_print_resp(), end='')
                    i += 1
                    tot += 1
                elif(j >= 55 and j <= test - 10):
                    print(get_print_old(), end='')
                    i += 1
                    tot += 1
                elif(j >= test - 9):
                    print(get_print_crit(), end='')
                    i += 1
                    tot += 1
                else:    
                    print(get_print_free(), end='')
                    i += 1
                    tot += 1
        print("/", end='')
        i = 0
        j += 1