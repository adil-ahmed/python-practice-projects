import random

# Function to check if input is a valid number and not zero
def get_valid_number(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value == 0:
                print("Input cannot be zero.")
                continue  # Ask for input again
            return value
        except ValueError:
            print("Invalid input! Please enter a valid non-zero number.")

# Get the maximum and minimum number from the user
maximum = get_valid_number("Enter the maximum range: ")

# Ensure minimum is smaller than maximum
while True:
    minimum = get_valid_number("Enter the minimum range: ")
    if minimum >= maximum:
        print("Minimum should be less than maximum. Please enter the minimum again.")
    else:
        break

# Generate a random number between minimum and maximum
original_number = random.randint(minimum, maximum)

# Guessing game loop
while True:
    try:
        guess_number = int(input(f"Guess the number between {minimum} and {maximum}: "))
        if guess_number > original_number:
            print("Too high!")
        elif guess_number < original_number:
            print("Too low!")
        else:
            print("Congratulations! You guessed the number.")
            break
    except ValueError:
        print("Please enter a valid number.")
