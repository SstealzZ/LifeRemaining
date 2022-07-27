import  sys, math, timeit, csv, datetime, date
from math import *

def get_days_alive(value):
    tmp = datetime.datetime.today()
    d = datetime.datetime(int(date.get_year(value)), int(date.get_month(value)), int(date.get_day(value)))
    c = tmp - d
    return (int(c.days))

def get_weeks_alive(value):
    tmp = datetime.datetime.today()
    d = datetime.datetime(int(date.get_year(value)), int(date.get_month(value)), int(date.get_day(value)))
    c = tmp - d
    return (int (c.days / 7))

def get_years_alive(value):
    tmp = datetime.datetime.today()
    d = datetime.datetime(int(date.get_year(value)), int(date.get_month(value)), int(date.get_day(value)))
    c = tmp - d
    return (int (c.days / 365))