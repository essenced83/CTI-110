# Essence Douglas
# 06/30/2024
# P3LAB Assignment
# This lab will calculate the most efficient number of dollars, quarters, dimes, nickels, and pennies needed to make the given amount of money.

def get_change():

    # input from user
    money = float(input("Enter an amount of money (float) with two decimal places: "))

    # convert to cents
    cents = int(money * 100)

    #calculate dollars, quarters, dimes, nickels, and pennies
    dollars = cents // 100
    cents %= 100

    quarters = cents // 25
    cents %= 25
    
    dimes = cents // 10
    cents %= 10

    nickels = cents // 5
    cents %= 5

    pennies = cents

    #output the result

    result = []

    if dollars > 0:
                  result.append(f"{dollars} {'dollar' if dollars == 1 else 'dollars'}")

    if quarters > 0:
                  result.append(f"{quarters} {'quarter' if quarters == 1 else 'quarters'}")

    if dimes > 0:
                  result.append(f"{dimes} {'dime' if dimes == 1 else 'dimes'}")

    if nickels > 0:
                  result.append(f"{nickels} {'nickel' if nickels == 1 else 'nickels'}")

    if pennies > 0:
                  result.append(f"{pennies} {'penny' if pennies == 1 else 'pennies'}")

    print("The most accurate number of each currency is: ")
    print(", ".join(result))

    

#call function
get_change()
         
