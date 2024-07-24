# Essence Douglas
# 7/21/2024
# P4HW1
# A program that collects scores and displays the score average. This program also displays a letter grade for the calculated average.

def main():
    print("Welcome to the Score Calculator!")
    print("This program calculates the average score after dropping the lowest score.")

    while True:
        # Step 2: Ask for number of scores
        num_scores = int(input("\nEnter the number of scores you would like to enter: "))
        
        # Validate if num_scores is positive
        while num_scores <= 0:
            print("Number of scores must be positive. Please enter again.")
            num_scores = int(input("Enter the number of scores you would like to enter: "))

        # Step 3: Initialize list to store scores
        scores = []

        # Step 4: Loop to collect scores
        for i in range(num_scores):
            while True:
                try:
                    score = int(input(f"Enter score #{i+1}: "))
                    if score < 0 or score > 100:
                        print("Score must be between 0 and 100. Please enter again.")
                    else:
                        scores.append(score)
                        break
                except ValueError:
                    print("Invalid input. Please enter a valid integer.")

        # Step 5: Find lowest score and remove it
        lowest_score = min(scores)
        scores.remove(lowest_score)

        # Step 6: Calculate average of modified scores list
        if len(scores) > 0:
            average_score = sum(scores) / len(scores)
        else:
            average_score = 0

        # Step 7: Determine letter grade
        if average_score >= 90:
            letter_grade = 'A'
        elif average_score >= 80:
            letter_grade = 'B'
        elif average_score >= 70:
            letter_grade = 'C'
        elif average_score >= 60:
            letter_grade = 'D'
        else:
            letter_grade = 'F'

        # Display results
        print("\nResults:")
        print(f"Lowest score entered: {lowest_score}")
        print(f"Score List after dropping lowest score: {scores}")
        print(f"Average score: {average_score:.2f}")
        print(f"Letter grade: {letter_grade}")

        # Step 8: Ask if user wants to run again
        run_again = input("\nDo you want to run the program again? (yes/no): ").lower()
        if run_again != "yes":
            break

    print("\nThank you for using the Score Calculator. Goodbye!")

if __name__ == "__main__":
    main()
