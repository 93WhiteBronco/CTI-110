# name redacted
# 9/25/2023
# This program takes four floating point inputs from the user, then outputs their product and average in integer and floating point formats

input_float_one = float(input("Enter the first floating point number: "))
input_float_two = float(input("Enter the second floating point number: "))
input_float_three = float(input("Enter the third floating point number: "))
input_float_four = float(input("Enter the fourth floating point number: "))

# this is a float, however the output will format it as an integer
product = input_float_one * input_float_two * input_float_three * input_float_four
# same here
average = (input_float_one + input_float_two + input_float_three + input_float_four) / 4

# VARNAME:.0f removes all digits after the ones place
print(f"(integer) product = {product:.0f}, average = {average:.0f}")
print(f"(float) product = {product:.3f}, average = {average:.3f}")  # VARNAME:.3f formats to the thousandths place
