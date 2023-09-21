# A brief description of the project
# 09/21/2023
# CTI-110 P1HW2 - Travel Expense
# Name
# https://www.youtube.com/watch?v=8n-ylg-pw6s

# ask user for inputs on budget, destination, and costs
# format the user's inputs
# display their remaining balance after all costs are subtracted from the budget

print("This program calculates and displays travel expenses")
budget_cost = int(input("\nEnter Budget: "))
destination = input("\nEnter your travel destination: ")
gas_cost = int(input("\nHow much do you think you will spend on gas? "))
hotel_cost = int(input("\nApproximately, how much will you need for accomodation/hotel? "))
food_cost = int(input("\nLast, how much do you need for food? "))
print("\n----------Travel Expenses----------")
print("Location:", destination, "\nInitial Budget:", budget_cost, "\n")
print("Fuel:", gas_cost)
print("Accomodation:", hotel_cost)
print("Food:", food_cost, "\n")

# add up all costs, THEN subtract the total costs from the budget
print("Remaining Balance:", budget_cost - (gas_cost + hotel_cost + food_cost))
