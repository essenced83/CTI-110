# Essence Douglas
# 07/21/2024
# Calculate Employee Pay

# Prompt user for inputs
employee_name = input("Enter name of employee: ")
hours_worked = float(input("Enter number of hours the employee worked this week: "))
pay_rate = float(input("Enter employee's pay rate: "))

# Calculate overtime hours and pay
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
else:
    overtime_hours = 0
    overtime_pay = 0

# Calculate pay for regular hours
regular_pay = min(hours_worked, 40) * pay_rate

# Calculate gross pay
gross_pay = regular_pay + overtime_pay

# Display the results
print("\nEmployee Name:", employee_name)
print("Pay Rate:", pay_rate)
print("Hours Worked:", hours_worked)
print("Overtime Hours:", overtime_hours)
print("Overtime Pay:", overtime_pay)
print("Pay for Regular Hours:", regular_pay)
print("Gross Pay:", gross_pay)
