def main():
    while True:
        # Ask the user to enter an integer
        num = int(input("Enter an integer (negative to quit): "))
        
        if num >= 0:
            # Display multiplication table from 1 to 12
            print(f"Multiplication table for {num}:")
            for i in range(1, 13):
                print(f"{num} x {i} = {num * i}")
        else:
            # Inform user about negative input and break the loop
            print("Negative values are not accepted. Exiting program.")
            break
        
        # Ask the user if they want to run the program again
        run_again = input("Do you want to run the program again? (yes/no): ").lower()
        if run_again != "yes":
            break

if __name__ == "__main__":
    main()
