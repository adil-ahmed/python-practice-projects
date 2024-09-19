import random

#set the maximum and minimum number
maximum = int(input("Enter the maximum range: "))
original_number = random.randint(1, 100)


while True:
    try:
        guess_number = int(input("Guess the number between 1 and 100: "))
        if(guess_number > original_number):
            print("Too high")
        elif(guess_number < original_number):
            print("Too low")
        else:
            print("Congratulations! You guessed the numnber")
            break
    except ValueError:
        print("Please enter a valid number")
