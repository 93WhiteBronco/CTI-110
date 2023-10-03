# CTI-110
# P3HW1 - Debugging
# name redacted
# This program takes a number grade, determines average and displays letter grade for average.

# Enter grades for six modules
mod_1 = float(input('Enter grade for Module 1: '))
mod_2 = float(input('Enter grade for Module 2: '))
mod_3 = float(input('Enter grade for Module 3: '))
mod_4 = float(input('Enter grade for Module 1: '))
mod_5 = float(input('Enter grade for Module 5: '))
mod_6 = float(input('Enter grade for Module 6: '))

# add grades entered to a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# calculate lowest, highest, sum, and average
lowest_grade = min(grades)
highest_grade = max(grades)
grade_sum = sum(grades)
average = grade_sum / len(grades)

# format and display outputs
print("------------Results------------")
print(f"Lowest Grade:\t\t{lowest_grade}")
print(f"Highest Grade:\t\t{highest_grade}")
print(f"Sum of Grades:\t\t{grade_sum}")
print(f"Average:\t\t{average:.2f}")
print("-------------------------------")
# determine letter grade for average
if average >= 90:
    print('Your grade is: A')
elif average >= 80:
    print('Your grade is: B')
elif average >= 70:
    print('Your grade is: C')
elif average >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F')





