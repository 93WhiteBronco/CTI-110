# TODO: comment framework
# This program takes a number grade , determines average and displays letter grade for average.

# Enter grades for six modules
mod_1 = int(input('Enter grade for Module 1: '))
mod_2 = int(input('Enter grade for Module 2: '))
mod_3 = int(input('Enter grade for Module 3: '))
mod_4 = int(input('Enter grade for Module 1: '))
mod_5 = int(input('Enter grade for Module 5: '))
mod_6 = int(input('Enter grade for Module 6: '))

# add grades entered to a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

lowest_grade = min(grades)
highest_grade = max(grades)
sum_of_grades = sum(grades)
average = sum_of_grades / len(grades)

print("----------Results----------")
print(f"Lowest Grade: {lowest_grade}")
print(f"Highest Grade: {highest_grade}")
print(f"Sum of Grades: {sum_of_grades}")
print(f"Average: {average}")

if average >= 90:
    print('Your grade is: A')
elif 80 <= average <= 89:
    print('Your grade is: B')
elif 70 <= average <= 79:
    print('Your grade is: C')
elif 60 <= average <= 69:
    print('Your grade is: D')
else:
    print('Your grade is: F')





