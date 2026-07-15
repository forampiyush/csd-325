
# Foram Dholariya
# June 15, 2026
# CSD-325 Module 2 Assignment
#
# Purpose: Calculate the average of three scores entered by the user.



def calculate_average(score1, score2, score3):
    # Calculate the average of the three scores
    average = (score1 + score2 + score3) / 3

    # Return the average value
    return average


def main():
    # Display the title of the program
    print("Average Score Calculator")

    # Get three scores from the user
    score1 = float(input("Enter first score: "))
    score2 = float(input("Enter second score: "))
    score3 = float(input("Enter third score: "))

    # Call the function to calculate the average
    
    # Display the average score
    print(f"The average score is {average:.2f}")


# Start the program
main()

