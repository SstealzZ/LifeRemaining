import calculate
def terminal_printer(gender, date):
    print("Days alive:")
    print(calculate.get_days_alive(date))
    print("Weeks alive:")
    print(calculate.get_weeks_alive(date))
    print("Years alive:")
    print(calculate.get_years_alive(date))