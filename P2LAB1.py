# name redacted
# 9/25/2023
# This program outputs the cost to drive X, Y, Z miles based on the cost of gas and MPG

miles_per_gallon = float(input("What is the car's efficiency in MPG?\n"))
dollars_per_gallon = float(input("How much does a gallon of gasoline cost?\n"))

# cost = (range / mpg) * cost per gallon of gasoline
cost_twenty_miles = (20 / miles_per_gallon) * dollars_per_gallon
cost_seventy_five_miles = (75 / miles_per_gallon) * dollars_per_gallon
cost_five_hundred_miles = (500 / miles_per_gallon) * dollars_per_gallon

# don't hyphenate five hundred
# VARNAME:.2f prints to hundredths place
print(f"Driving twenty miles: {cost_twenty_miles:.2f}\nDriving seventy-five miles: {cost_seventy_five_miles:.2f}\nDriving five hundred miles: {cost_five_hundred_miles:.2f}")
