import  sys, math, timeit, csv, datetime
from math import *

def get_day(value):
    if (value[0] == '0'):
        return (value[1])
    else:
        return (value[0] + value[1])

def get_month(value):
    if (value[3] == '0'):
        return (value[4])
    else:
        return (value[3] + value[4])

def get_year(value):
    return(value[6] + value[7] + value[8] + value[9])