def days_to_units(number_of_days, conversion_unit):
    if conversion_unit == "hours":
        return f"{number_of_days} days are {number_of_days * 24} {conversion_unit}"
    elif conversion_unit == "minutes":
        return f"{number_of_days} days are {number_of_days * 24 * 60} {conversion_unit}"
    else:
        return "unsupported unit"


def validate_and_execute(days_and_unit_dic):
    try:
        user_input_number = int(days_and_unit_dic["days"])
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number, days_and_unit_dic["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print("You entered a 0, please enter a valid positive number")
        else:
            print("ou entered a negative number, no conversation for you!")
    except ValueError:
        print("our input is not a valid number. Don't ruin my program!")


user_input_message = "enter number of days and conversion unit!(hours or minutes)\n"

