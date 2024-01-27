print("200 is a great number")
print(2)
print(3.5)
print("20 das are " + str(50) + " minutes ")


calculation_to_units = 24 * 60
name_of_unit = "seconds"


def days_to_units(number_of_days):
    print(f"{number_of_days} days are {number_of_days * calculation_to_units} {name_of_unit}")


days_to_units(6)


def return_days_to_units(return_number_of_days):
    if return_number_of_days > 0:
        return f"{return_number_of_days} days are {return_number_of_days * calculation_to_units} {name_of_unit}"
    else:
        return "You entered a negative value, so no conversation for you"


def validate_and_execute():
    if user_input.isdigit():
        print("es")
    else:
        print("please enter a valid number")


def validate_and_execute_try():
    try:
        print("es")
    except ValueError:
        print("please enter a valid number")


user_input = ""
while user_input != "exit":
    user_input = input("Hey user, enter a number of das and I will convert it to hours!\n")
    # user_input_number = int(user_input)


# calculated_value = return_days_to_units(user_input_number)
# print(calculated_value)
# my_var = return_days_to_units(4)
# print(my_var)

