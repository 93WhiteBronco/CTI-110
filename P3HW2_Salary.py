# CTI-110
# P3HW2 - Salary
# name redacted
# 10/2/2023
# This program takes name, hours worked, and hourly wage, then calculates gross pay, including overtime

# get name, hours, wage
# boolean has worked = true if hours > 40, else false
# if has_worked_overtime then
# overtime pay = overtime hours * wage * 1.5
# regular pay = hours - overtime hours * wage
# output name, hours, wage, overtime hours, overtime pay, regular pay, gross pay

employee_name = input("Enter employee's name: ")
this_week_work_hours = float(input("Enter number of hours worked: "))
employee_pay_rate = float(input("Enter employee's pay rate: "))

has_worked_overtime = True if this_week_work_hours > 40 else False  # python has no real ternary operator
overtime_hours = this_week_work_hours - 40
regular_pay = 0
overtime_pay = 0

if has_worked_overtime:  # this program is basically branchless but whatever
    overtime_pay = (overtime_hours * employee_pay_rate) * 1.5

regular_pay = (this_week_work_hours - overtime_hours) * employee_pay_rate  # if overtime hours is negative then it becomes addition
gross_pay = regular_pay + overtime_pay

print("---------------------------------")
print(f"Employee name: {employee_name}\n")

print("Hours Worked\tPay Rate\tOverTime\tOverTime Pay\tRegHour Pay\tGross Pay")
print("-------------------------------------------------------------------------------------------------------")
print(f"{this_week_work_hours}\t\t{employee_pay_rate}\t\t{overtime_hours}\t\t{overtime_pay:.2f}\t\t${regular_pay:.2f}\t\t${gross_pay:.2f}")
