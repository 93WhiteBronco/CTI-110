# CTI-110
# P2HW2 - List
# name redacted
# 9/25/2023
# This program introduces python lists

# Pseudocode:
# store inputs into six variables
# add all inputs into all_grades_list
# store results of max(), min(), sum(), and the average into four more variables
# output results of max(), min(), sum(), and average

mod_one_grade = float(input("Enter grade for module 1: "))
mod_two_grade = float(input("Enter grade for module 2: "))
mod_three_grade = float(input("Enter grade for module 3: "))
mod_four_grade = float(input("Enter grade for module 4: "))
mod_five_grade = float(input("Enter grade for module 5: "))
mod_six_grade = float(input("Enter grade for module 6: "))

# create a list, don't append six times thats weird lil bro
all_grades_list = [
    mod_one_grade,
    mod_two_grade,
    mod_three_grade,
    mod_four_grade,
    mod_five_grade,
    mod_six_grade
]

print("\n----------Results----------")

highest_grade = max(all_grades_list)
lowest_grade = min(all_grades_list)
sum_of_grades = sum(all_grades_list)
avg_of_grades = sum_of_grades / len(all_grades_list)  # no imports needed, save memory

# only the average may have hundredths place per homework instructions
print(f"Lowest Grade: {lowest_grade:.1f}", f"\nHighest Grade: {highest_grade:.1f}", f"\nSum of Grades: {sum_of_grades:.1f}", f"\nAverage: {avg_of_grades:.2f}")
print("---------------------------")
