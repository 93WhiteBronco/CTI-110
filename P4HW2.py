# CTI-110
# P4HW2 - Salary Calculator
# name redacted
# 10/10/2023
# This program takes inputs for multiple employees and calculates total amount paid out to all employees

employee_name = input("Enter employee's name or \"Done\" to terminate: ")
total_employees = 0
total_normal_pay = 0
total_overtime_pay = 0

while employee_name != "Done":
    this_week_work_hours = float(input(f"How many hours did {employee_name} work? "))
    employee_pay_rate = float(input(f"What is {employee_name}'s pay rate? "))

    has_worked_overtime = True if this_week_work_hours > 40 else False  # python has no real ternary operator
    
    overtime_hours = this_week_work_hours - 40
    this_employee_overtime_pay = 0
    this_employee_normal_pay = 0
    
    if this_week_work_hours <= 40:
        this_employee_normal_pay = this_week_work_hours * employee_pay_rate
        overtime_hours = 0
    else:
        this_employee_normal_pay = (this_week_work_hours - overtime_hours) * employee_pay_rate
        this_employee_overtime_pay = (overtime_hours * employee_pay_rate) * 1.5

    gross_pay = this_employee_normal_pay + this_employee_overtime_pay

    total_employees += 1
    total_normal_pay += this_employee_normal_pay
    total_overtime_pay += this_employee_overtime_pay

    print(f"\nEmployee name: {employee_name}\n")

    print("Hours Worked\tPay Rate\tOverTime\tOverTime Pay\tRegHour Pay\tGross Pay")
    print("-------------------------------------------------------------------------------------------------------")
    print(f"{this_week_work_hours:.1f}\t\t{employee_pay_rate:.2f}\t\t{overtime_hours:.1f}\t\t{this_employee_overtime_pay:.2f}\t\t${this_employee_normal_pay:.2f}\t\t${gross_pay:.2f}\n\n")

    employee_name = input("Enter employee's name or \"Done\" to terminate: ")

print("\nTotal number of employees entered:", total_employees)
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: ${total_normal_pay:.2f}")
print(f"Total amount paid in gross: ${(total_normal_pay + total_overtime_pay):.2f}")
