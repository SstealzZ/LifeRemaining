import  sys, math, timeit, csv, datetime, date
from math import *

def get_date_of_birth(value):
    d = datetime.datetime(int(date.get_year(value)), int(date.get_month(value)), int(date.get_day(value)))
    return (d.date())

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

def get_date_of_death(opt, value):
    ttd = 0
    if (opt == "-m"):
        ttd = 79
    if (opt == "-f"):
        ttd = 85
    d = datetime.datetime(int(date.get_year(value)) + ttd, int(date.get_month(value)), int(date.get_day(value)))
    return (d.date())

def get_days_remaining(opt, value):
    ttd = 0
    if (opt == "-m"):
        ttd = 79
    if (opt == "-f"):
        ttd = 85
    db = tmp = datetime.datetime.today()
    dd = datetime.datetime(int(date.get_year(value)) + ttd, int(date.get_month(value)), int(date.get_day(value)))
    c = dd - db
    return (int(c.days))

def get_weeks_remaining(opt, value):
    ttd = 0
    if (opt == "-m"):
        ttd = 79
    if (opt == "-f"):
        ttd = 85
    db = tmp = datetime.datetime.today()
    dd = datetime.datetime(int(date.get_year(value)) + ttd, int(date.get_month(value)), int(date.get_day(value)))
    c = dd - db
    return (int(c.days / 7))

def get_years_remaining(opt, value):
    ttd = 0
    if (opt == "-m"):
        ttd = 79
    if (opt == "-f"):
        ttd = 85
    db = tmp = datetime.datetime.today()
    dd = datetime.datetime(int(date.get_year(value)) + ttd, int(date.get_month(value)), int(date.get_day(value)))
    c = dd - db
    return (int(c.days / 365))

    