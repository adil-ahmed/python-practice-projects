import random
counter = 0
while True:
    response = input("Roll the dice? (y/n): ").lower()
    if response == 'y':
        counter = counter + 1
        
        rolls = {}  # Dictionary to store the dice rolls
        # Initialize the number variable
        number = 0

        # Keep asking for a valid number (greater than 0)
        while number <= 0:
            number = int(input("How many dice you want to roll? "))
            if number <= 0:
                print("Insert a positive number greater than 0")

        # Roll the dice and store the results
        for i in range(1, number + 1):
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            rolls[i] = (dice1, dice2)  # Store the dice roll results in the dictionary

        # Print the stored dice rolls
        for roll_number, dice_values in rolls.items():
            print(f'Roll {roll_number}: {dice_values}')
    
    elif response == 'n':
        time_word = "time" if counter == 1 else "times"
        print(f'You rolled the dice {counter} {time_word}. Thanks for playing. Have a good day.')
        break
        
    
    else:
        print("Invalid choice!")

