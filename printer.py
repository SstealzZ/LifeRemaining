import calculate
def terminal_printer(gender, date):
    print("--------------------------------------------------------------------------")

    print("Date of birth:")
    print(calculate.get_date_of_birth(date))
    
    print("--------------------------------------------------------------------------")
    
    print("Days alive:")
    print(calculate.get_days_alive(date))
    print("Weeks alive:")
    print(calculate.get_weeks_alive(date))
    print("Years alive:")
    print(calculate.get_years_alive(date))

    print("--------------------------------------------------------------------------")

    print("Estimated date of death:")
    print(calculate.get_date_of_death(gender, date))
    print("Estimated days Remaining")
    print(calculate.get_days_remaining(gender, date))
    print("Estimated weeks Remaining")
    print(calculate.get_weeks_remaining(gender, date))
    print("Estimated years Remaining")
    print(calculate.get_years_remaining(gender, date))

    print("--------------------------------------------------------------------------")