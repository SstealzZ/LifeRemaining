import calculate, gui_lifeused
from my_colors import my_colors

def terminal_printer(gender, date):
    print(my_colors.LightYellow + "--------------------------------------------------------------------------" + my_colors.ResetAll)

    print("Date of birth:")
    print(calculate.get_date_of_birth(date))
    
    print(my_colors.LightYellow + "--------------------------------------------------------------------------" + my_colors.ResetAll)

    print(my_colors.LightGreen + "Days alive:" + my_colors.White)
    print(calculate.get_days_alive(date))
    print(my_colors.LightGreen + "Weeks alive:" + my_colors.White)
    print(calculate.get_weeks_alive(date))
    print(my_colors.LightGreen + "Years alive:" + my_colors.White)
    print(calculate.get_years_alive(date))

    print(my_colors.LightYellow + "--------------------------------------------------------------------------" + my_colors.ResetAll)

    print(my_colors.LightRed + "Estimated date of death:" + my_colors.White)
    print(calculate.get_date_of_death(gender, date))
    print(my_colors.LightRed + "Estimated days Remaining:" + my_colors.White)
    print(calculate.get_days_remaining(gender, date))
    print(my_colors.LightRed + "Estimated weeks Remaining:" + my_colors.White)
    print(calculate.get_weeks_remaining(gender, date))
    print(my_colors.LightRed + "Estimated years Remaining:" + my_colors.White)
    print(calculate.get_years_remaining(gender, date))

    print(my_colors.LightYellow + "--------------------------------------------------------------------------" + my_colors.ResetAll)

    print(my_colors.LightBlue + "Life Storage:")
    print(my_colors.LightRed + "Life use: {:.2f}%".format(calculate.get_life_used(gender, date)))
    print(my_colors.LightGreen + "Life remaining: {:.2f}%".format(100 - calculate.get_life_used(gender, date)))
    print(my_colors.LightYellow + "Life before being old: {} years".format(55 - calculate.get_years_alive(date)))
    print(my_colors.LightBlue + "Life before taking on real responsibilities: {} years".format(30 - calculate.get_years_alive(date)))

    print(my_colors.LightYellow + "--------------------------------------------------------------------------" + my_colors.ResetAll)

    gui_lifeused.gui(gender, date)