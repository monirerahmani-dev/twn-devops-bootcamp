#import helper as h
# helper.validate_and_execute(days_and_unit_dic)
from helper import validate_and_execute, user_input_message


user_input = ""
while user_input != "exit":
    user_input = input(user_input_message)
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    days_and_unit_dic = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(days_and_unit_dic)
    print(type(days_and_unit_dic))
    validate_and_execute(days_and_unit_dic)
