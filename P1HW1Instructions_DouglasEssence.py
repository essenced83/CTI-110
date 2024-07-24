# Essence Douglas
# 6/16/2024
# P1HW1 Instructions
# This program takes user input for base and exponent values, calculates the power, and performs basic arithmetic operations.

# Part 1: Calculating Exponents
base_value = int(input("Enter an integer as the base value: "))
exponent_value = int(input("Enter an integer as the exponent: "))
result = base_value ** exponent_value
print(f"{base_value} raised to the power of {exponent_value} is {result}")

# Part 2: Addition and Subtraction
starting_integer = int(input("Enter a starting integer: "))
integer_to_add = int(input("Enter an integer to add: "))
integer_to_subtract = int(input("Enter an integer to subtract: "))
final_result = starting_integer + integer_to_add - integer_to_subtract
print(f"{starting_integer} + {integer_to_add} - {integer_to_subtract} is equal to {final_result}")
