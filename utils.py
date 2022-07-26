import  sys, math, timeit, csv
from math import *

def get_number(char):
    try:
        nbr = int(char)
    except:
        sys.stdout.write("Invalid argument, use -h for help\n")
        exit(84)
    return nbr