# Essence Douglas
# 6/16/2024
# P1HW2 Instructions
# This program calculates and displays the remaining budget after accounting for travel expenses.

# Ask user to enter their budget
budget = float(input("Enter your budget: "))

# Ask user to enter travel destination
destination = input("Enter your travel destination: ")

# Ask for amount they will spend on gas
gas_expense = float(input("Amount you will spend on gas: "))

# Ask for amount they will spend on accommodations
accommodation_expense = float(input("Amount you will spend on accommodation: "))

# Ask for amount they will spend on food
food_expense = float(input("Amount you will spend on food: "))

# Add expenses
total_expenses = gas_expense + accommodation_expense + food_expense

# Subtract expenses from budget
remaining_budget = budget - total_expenses

# Display results
print(f"Destination: {destination}")
print(f"Total Expenses: ${total_expenses:.2f}")
print(f"Remaining Budget: ${remaining_budget:.2f}")
