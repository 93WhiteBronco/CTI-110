# name redacted
# 9/27/2023
# This program asks the user to enter a year, then evaluates whether it is a leap year

input_year = int(input("Enter a year: "))
is_leap_year = False

not_century_year = bool(input_year % 100)  # if the remainder is 0, then it IS a century year (1400, 1600, etc), which is then converted to a boolean (0 == False)

if not input_year % 400:  # 1200, 1600, 2000 are century years AND leap years
    is_leap_year = True
else:
    if not input_year % 4 and not_century_year:  # if the remainder is 0 and the year is not a century year, the given year is a leap year
        is_leap_year = True

print(f"{input_year} - {'leap year' if is_leap_year else 'not a leap year'}")  # ternary operator to provide output to user
