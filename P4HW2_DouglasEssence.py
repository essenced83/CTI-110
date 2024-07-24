# Essence Douglas
# 07/22/2024
# P4HW2
# The program however will calculate gross pay for multiple employees, determined by user, and also calculates total amount paid for overtime, total amount paid for regular pay and total amount paid for all employees.

def main():
    print("Welcome to the Employee Pay Calculator!")
    print("This program calculates gross pay for multiple employees.")

    # Initialize variables to store totals
    overtime_total = 0
    regular_pay_total = 0
    gross_pay_total = 0
    employee_count = 0

    while True:
        # Step 3a: Prompt user to enter employee name
        employee_name = input("\nEnter employee name (type 'Done' to finish): ").strip()

        # Step 3b: Check if user wants to terminate the program
        if employee_name.lower() == "done":
            break

        # Step 3c: Ask for pay rate and hours worked
        try:
            pay_rate = float(input("Enter pay rate per hour: "))
            hours_worked = float(input("Enter hours worked this week: "))

            # Step 3d: Calculate overtime pay if applicable
            if hours_worked > 40:
                overtime_hours = hours_worked - 40
                overtime_pay = overtime_hours * (pay_rate * 1.5)
            else:
                overtime_pay = 0

            # Step 3e: Calculate regular pay
            regular_pay = min(hours_worked, 40) * pay_rate

            # Step 3f: Calculate gross pay
            gross_pay = regular_pay + overtime_pay

            # Step 3g: Update totals
            overtime_total += overtime_pay
            regular_pay_total += regular_pay
            gross_pay_total += gross_pay

            # Step 3h: Increment employee count
            employee_count += 1

        except ValueError:
            print("Invalid input. Please enter numeric values for pay rate and hours worked.")

    # Step 4: Display results
    print("\nPayroll Summary:")
    print(f"Total overtime paid: ${overtime_total:.2f}")
    print(f"Total regular pay: ${regular_pay_total:.2f}")
    print(f"Total gross pay: ${gross_pay_total:.2f}")
    print(f"Number of employees entered: {employee_count}")

    print("\nThank you for using the Employee Pay Calculator. Goodbye!")

if __name__ == "__main__":
    main()
